
def file_input(file_name):
    open_file = open(file_name, 'r')
    activities = []
    count = 0
    for line in open_file:
        if count == 0:
            num_act = int(line)
        elif count == 1:
            time_budget = line
        else:
            activities.append(line)
        count += 1

    # Extract the time and budget from line 2
    time_av = time_budget.split(" ")[0]
    budget_av = time_budget.split(" ")[1]

    # Output file metadata
    print(f"Num of activities: {num_act} ")
    print(f"Time: {time_av} ")
    print(f"Budget: {budget_av}")
    activ_dict = {0:int(num_act), 1:int(time_av), 2:int(budget_av)}

    for act in enumerate(activities):
        act_list = act[1].strip().split(" ")

        activ_dict[act[0]+3] = [str(act_list[0]), int(act_list[1]), int(act_list[2]), int(act_list[3])]

    return activ_dict

print(file_input("./Input_Files/input_10.txt"))