"""
This Python module houses the dynamic programming method to ECM1414 Data Structures
and Algorithms Coursework using the cost as a limitation.
"""

import time

def dynamic_subsets(activity_list: list[tuple]) -> list[tuple]:
    """
    This function generates all possible subsets of a given
    list using dynamic programming algorithm.
    """
    av_budget = activity_list[0][1]
    activities = activity_list[1:]
    num_activities = len(activities)

    dp_table = [0] * (av_budget + 1)

    for act in activities:
        act_cost = act[2]
        act_enjoy = act[3]
        for i in range(av_budget, act_cost-1, -1):
            dp_table[i] = max(dp_table[i], dp_table[i - act_cost] + act_enjoy)

    subsets = []
    budget = av_budget

    for i in range(num_activities-1,-1,-1):
        act_cost = activities[i][2]
        act_enjoy = activities[i][3]

        if budget >= act_cost and dp_table[budget] == dp_table[budget-act_cost] + act_enjoy:
            subsets.append(activities[i])
            budget = budget - act_cost
    return subsets

def file_to_list(file_path):
    """
    This function transforms the file input into a list of activities.
    """
    act_list = []
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    time_budget = list(map(int, lines[1].split()))
    av_budget = time_budget[1]
    act_list.append((0, av_budget))

    for line in lines[2:]:
        parts = line.split()
        name = parts[0]
        act_time = int(parts[1])
        cost = int(parts[2])
        enjoy = int(parts[3])
        act_list.append((name, act_time, cost, enjoy))

    return act_list

start = time.time()
file = file_to_list('../Input_Files/input_100.txt')
optimal_subsets = dynamic_subsets(file)

print(f"Length of subsets: {len(optimal_subsets)}")
print(f"Selected activities: {optimal_subsets}")
end = time.time()
print("Time taken:", end - start)
