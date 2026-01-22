
def file_input(file_name):
    open_file = open(file_name, 'r')
    activities = []
    count = 0
    for line in open(file_name, 'r'):
        if count == 0:
            num_act = int(line)
        elif count == 1:
            time_budget = line
        else:
            activities.append(line)
        count += 1


    print(f"Num of activities: {num_act} ")
    print(f"Time: {time_budget.split(" ")[0]} ")
    print(f"Budget: {time_budget.split(" ")[1]}")
    print(f"Activities: {activities}")


file_input("Sample Input Files/input_10.txt")