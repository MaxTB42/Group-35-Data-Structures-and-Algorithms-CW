from file_input import file_input
from itertools import combinations
import math

def generate_subs(activity_dict, length):
    items = list(activity_dict.values())
    activity_dict_short = items[3:]
    subsets = list(combinations(activity_dict_short, length))
    i=0
    for set in subsets:
        i += 1

    print(f"Number of subsets: {i}")
    print(f"Combinations:{math.comb(10,length)}")

    return subsets

def total_subsets(subsets):
    subsets_sum = []

    for set in subsets:
        total_time_set = 0
        total_cost_set = 0
        total_enjoy_set = 0
        act = []

        for item in set:
            total_time_set += item[1]
            total_cost_set += item[2]
            total_enjoy_set += item[3]
            act.append(item[0])

        set_sum = [total_time_set, total_cost_set, total_enjoy_set, act]
        subsets_sum.append(set_sum)
    return subsets_sum



def verify_subsets(subsets_sum, activity_dict):
    total_cost = activity_dict[2]
    print(f"Orginal subsets: {len(subsets_sum)}")
    for set in subsets_sum:
        if set[1] > total_cost:
            subsets_sum.remove(set)
    print(f"Verified subsets: {len(subsets_sum)}")
    return subsets_sum


activity_dict = file_input("../Input_Files/input_10.txt")
subsets = generate_subs(activity_dict, 4)
subset_sum = total_subsets(subsets)
subset_sum_checked = verify_subsets(subset_sum, activity_dict)

sorted_subsets= sorted(subset_sum_checked, key=lambda x: x[2], reverse=True)
print(f"Sorted subsets: {sorted_subsets}")