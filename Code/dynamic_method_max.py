import file_input_new as fi
import time

def dynamic_subsets(list):
    num_activities = list[0][0]
    av_budget = list[0][2]
    av_time = list[0][1]
    total_subsets = 2**num_activities

    subsets = [[]]

    for act in list[1:]:
        act_cost = act[2]
        inner_set = []

        for sub in subsets:
            current_sum = sum(item[2] for item in sub)
            if current_sum + act_cost <= av_budget:
                entry = sub + [act]
                inner_set.append(entry)

        subsets.extend(inner_set)
    return subsets

start = time.time()
print(len(dynamic_subsets(fi.file_input("../Input_Files/input_large.txt"))))
end = time.time()
print(end - start)