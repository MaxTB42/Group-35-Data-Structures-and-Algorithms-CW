
def file_input(file_name):
    activity_file = open(file_name, 'r')
    activities = []
    count = 0

    # Decode each line
    for line in activity_file:
        if count == 0:
            number_of_activities = int(line)
        elif count == 1:
            time_and_budget = line
        else:
            activities.append(line)
        count += 1
    
    # Close the file
    activity_file.close()

    # Extract the time and budget from line 2
    time_and_budget_separated = time_and_budget.split(' ')
    time_available = time_and_budget_separated[0]
    budget_available = time_and_budget_separated[1]

    # Output file metadata
    print(f"Num of activities: {number_of_activities}")
    print(f"Time: {time_available}")
    print(f"Budget: {budget_available}")

    # Initialise the activity dictionary with the file metadata
    activity_dict = {0:int(number_of_activities), 1:int(time_available), 2:int(budget_available)}

    # Iterate over each activity extracted from the input file
    for activity in enumerate(activities):
        # Separate out the activity attributes
        activity_attributes = activity[1].strip().split(" ")
        # Add this extracted activity to the dictionary of activities
        activity_dict[activity[0] + 3] = [str(activity_attributes[0]), int(activity_attributes[1]),
                                          int(activity_attributes[2]), int(activity_attributes[3])]

    return activity_dict

print(file_input("./Input_Files/input_10.txt"))