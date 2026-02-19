from dataclasses import dataclass
from typing import List, Tuple
import time

@dataclass(frozen=True)
class Activity:
    name: str
    time_hours: int
    cost_gbp: int
    enjoyment: int

@dataclass
class Solution:
    selected: List[Activity]
    total_time: int
    total_cost: int
    total_enjoyment: int

def solve_bruteforce(activities: List[Activity], max_time: int, max_budget: int) -> Solution:
    """
    Exhaustive search over all subsets. O(2^n).
    """
    n = len(activities)
    best = Solution([], 0, 0, 0)

    for mask in range(1 << n):
        t = c = e = 0
        picked: List[Activity] = []
        for i in range(n):
            if (mask >> i) & 1:
                a = activities[i]
                t += a.time_hours
                c += a.cost_gbp
                e += a.enjoyment
                if t > max_time or c > max_budget:
                    break
                picked.append(a)

        if t <= max_time and c <= max_budget:
            # tie-break: higher enjoyment, then lower cost, then lower time
            if (e > best.total_enjoyment or
                (e == best.total_enjoyment and c < best.total_cost) or
                (e == best.total_enjoyment and c == best.total_cost and t < best.total_time)):
                best = Solution(picked, t, c, e)

    return best


def solve_dp(activities: List[Activity], max_time: int, max_budget: int) -> Solution:
    """
    0/1 knapsack with TWO constraints (time + budget).
    DP[t][b] = max enjoyment achievable.
    Reconstructs chosen activities.
    Time: O(n * max_time * max_budget)
    Space: O(max_time * max_budget) + parent pointers.
    """
    # dp[t][b] = enjoyment
    dp = [[0] * (max_budget + 1) for _ in range(max_time + 1)]
    # parent pointers for reconstruction: store (prev_t, prev_b, idx) or None
    parent = [[None] * (max_budget + 1) for _ in range(max_time + 1)]

    for idx, a in enumerate(activities):
        # iterate backwards to enforce 0/1 choice
        for t in range(max_time, a.time_hours - 1, -1):
            for b in range(max_budget, a.cost_gbp - 1, -1):
                cand = dp[t - a.time_hours][b - a.cost_gbp] + a.enjoyment
                if cand > dp[t][b]:
                    dp[t][b] = cand
                    parent[t][b] = (t - a.time_hours, b - a.cost_gbp, idx)

    best_t = best_b = 0
    best_e = 0
    for t in range(max_time + 1):
        for b in range(max_budget + 1):
            if dp[t][b] > best_e:
                best_e = dp[t][b]
                best_t, best_b = t, b

    # reconstruct
    selected: List[Activity] = []
    t, b = best_t, best_b
    used = set()
    while parent[t][b] is not None:
        pt, pb, idx = parent[t][b]
        if idx in used:
            break
        used.add(idx)
        selected.append(activities[idx])
        t, b = pt, pb

    selected.reverse()
    total_time = sum(x.time_hours for x in selected)
    total_cost = sum(x.cost_gbp for x in selected)
    total_enjoyment = sum(x.enjoyment for x in selected)

    return Solution(selected, total_time, total_cost, total_enjoyment)




def _format_activity(a: Activity) -> str:
    return f"- {a.name} ({a.time_hours} hours, £{a.cost_gbp}, enjoyment {a.enjoyment})"

def _solutions_equivalent(a: Solution, b: Solution) -> bool:
    # identical enjoyment/time/cost is typically what coursework wants.
    # (Exact same subset may vary if there are ties.)
    return (a.total_enjoyment == b.total_enjoyment and
            a.total_time == b.total_time and
            a.total_cost == b.total_cost)

def print_results(
    activities: List[Activity],
    max_time: int,
    max_budget: int,
    input_filename: str = "N/A"
) -> None:
    print("=" * 40 + " EVENT PLANNER - RESULTS " + "=" * 40)
    print(f"Input File: {input_filename}")
    print(f"Available Time: {max_time} hours")
    print(f"Available Budget: £{max_budget}")
    print()

    t0 = time.perf_counter()
    brute = solve_bruteforce(activities, max_time, max_budget)
    t1 = time.perf_counter()
    brute_seconds = t1 - t0

    print("--- BRUTE FORCE ALGORITHM ---")
    print("Selected Activities:")
    if brute.selected:
        for a in brute.selected:
            print(_format_activity(a))
    else:
        print("- (none)")
    print(f"Total Enjoyment: {brute.total_enjoyment}")
    print(f"Total Time Used: {brute.total_time} hours")
    print(f"Total Cost: £{brute.total_cost}")
    print(f"Constraint Summary: Available Time: {max_time} hours | Time Used: {brute.total_time} hours")
    print(f"Constraint Summary: Available Budget: £{max_budget} | Budget Used: £{brute.total_cost}")
    print(f"Execution Time: {brute_seconds:.6f} seconds")
    print()

    t0 = time.perf_counter()
    dp = solve_dp(activities, max_time, max_budget)
    t1 = time.perf_counter()
    dp_seconds = t1 - t0

    print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
    print("Selected Activities:")
    if dp.selected:
        for a in dp.selected:
            print(_format_activity(a))
    else:
        print("- (none)")
    print(f"Total Enjoyment: {dp.total_enjoyment}")
    print(f"Total Time Used: {dp.total_time} hours")
    print(f"Total Cost: £{dp.total_cost}")
    print(f"Constraint Summary: Available Time: {max_time} hours | Time Used: {dp.total_time} hours")
    print(f"Constraint Summary: Available Budget: £{max_budget} | Budget Used: £{dp.total_cost}")
    print(f"Execution Time: {dp_seconds:.6f} seconds")
    print()

    print("--- ALGORITHM COMPARISON ---")
    if _solutions_equivalent(brute, dp):
        print("Result Check: Both algorithms produced the same optimal totals.")
    else:
        print("Result Check:  Mismatch detected!")
        print(f"Brute totals: enjoyment={brute.total_enjoyment}, time={brute.total_time}, cost={brute.total_cost}")
        print(f"DP totals:    enjoyment={dp.total_enjoyment}, time={dp.total_time}, cost={dp.total_cost}")

    # Simple speed comparison line (as requested)
    print(f"Performance: Brute force took approximately {brute_seconds:.4f} seconds; "
          f"dynamic programming took approximately {dp_seconds:.4f} seconds.")
    print("=" * 94)

# Example usage 

if __name__ == "__main__":
    activities = [
        Activity("Campus-Tour", 2, 20, 50),
        Activity("Game-Night", 3, 80, 120),
        Activity("Museum-Trip", 4, 100, 150),
        Activity("Pizza-Workshop", 2, 60, 100),
        Activity("Hiking", 5, 30, 140),
    ]

    print_results(
        activities=activities,
        max_time=10,
        max_budget=200,
        input_filename="input_small.txt"
    )
