"""
This Python module houses the dynamic programming method to ECM1414 Data Structures
and Algorithms Coursework using the cost as a limitation.
"""

import time
import file_input_new as fi

def dynamic_subsets(activity_list: tuple[tuple]) -> list[list[tuple]]:
    """
    This function generates all possible subsets of a given
    list using dynamic programming algorithm.
    """
    av_budget = activity_list[0][2]
    subsets = [([], 0)]

    for act in activity_list[1:]:
        act_cost = act[2]
        inner_set = []

        for sub, curr_cost in subsets:
            if curr_cost + act_cost <= av_budget:
                entry = (sub + [act], curr_cost + act_cost)
                inner_set.append(entry)
        subsets.extend(inner_set)
    return [item[0] for item in subsets]

start = time.time()
print(f"Length of subsets {len(dynamic_subsets(fi.file_input('../Input_Files/input_10.txt')))}")
end = time.time()
print(end - start)
