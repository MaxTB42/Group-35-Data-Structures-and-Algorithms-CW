from file_input import file_input
from itertools import combinations

def generate_subs(activity_dict):
    combinations(activity_dict[12], 2)
    print(activity_dict)
    print("done")

generate_subs(file_input("./Input_Files/input_10.txt"))