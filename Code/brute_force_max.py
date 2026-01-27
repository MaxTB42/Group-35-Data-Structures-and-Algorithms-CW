from file_input import file_input
from itertools import combinations
import math
import time

def generate_subs(dict, length):
    #Isolate activities
    items = list(dict.values())
    activity_dict_short = items[3:]
    #Generate subsets
    subsets = list(combinations(activity_dict_short, length))
    #Verifing subset count
    print(f"Number of subsets: {len(subsets)}")
    print(f"Combinations:{math.comb(10,length)}")
    return subsets

def total_subsets(subsets):
    subsets_sum = []
    #Iterating through each set of activities
    for set in subsets:
        total_time_set = 0
        total_cost_set = 0
        total_enjoy_set = 0
        act = []

        #Iterating through each activity
        #Creating sum for time, cost and enjoyment
        for item in set:
            total_time_set += item[1]
            total_cost_set += item[2]
            total_enjoy_set += item[3]
            act.append(item[0])

        #Creating a tuple for each set with totals
        set_sum = [total_time_set, total_cost_set, total_enjoy_set, act]
        subsets_sum.append(set_sum)
    return subsets_sum



def verify_subsets(subsets_sum, activity_dict):
    total_cost = activity_dict[2]
    print(f"Original subsets: {len(subsets_sum)}")
    #Checking whether each set is within budget
    verified_subsets = []
    for subset in subsets_sum:
        if subset[1] <= total_cost:
            verified_subsets.append(subset)
    print(f"Verified subsets: {len(subsets_sum)}")
    return verified_subsets

start_time = time.time()
activity_dict = file_input("../Input_Files/input_10.txt")
subsets = []
for i in range(10):
    subsets.extend(generate_subs(activity_dict, i))

subset_sum = total_subsets(subsets)
subset_sum_checked = verify_subsets(subset_sum, activity_dict)

#Sorting list by enjoyment
sorted_subsets= sorted(subset_sum_checked, key=lambda x: x[2], reverse=True)
print(f"Most enjoyment: {sorted_subsets[0]}")
end_time = time.time()

print(f"Time taken: {end_time - start_time:.4f}")