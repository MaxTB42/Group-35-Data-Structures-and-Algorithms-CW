"""
This module is used to read and parse the file of activities.
"""

def file_input(file_name: str) -> tuple[tuple]:
    """
    This function reads and parses the input file.
    """

    # Initialising variables
    activities_from_file = []
    time_and_budget = ''
    number_of_activities = 0

    # Read the file contents
    with open(file_name, 'r', encoding='utf-8') as activity_file:
        # Extract the number of activities and time/budget lines
        number_of_activities = int(activity_file.readline())
        time_and_budget = activity_file.readline()
        # Read the rest of the file and split into each activity line
        activities_from_file += activity_file.read().splitlines()

    # Extract the time and budget from line 2
    time_and_budget_separated = time_and_budget.strip().split(' ')
    time_available = time_and_budget_separated[0]
    budget_available = time_and_budget_separated[1]

    # Initialise the activity list with the file metadata
    activities = [(int(number_of_activities), int(time_available), int(budget_available))]

    # Iterate over each activity extracted from the input file
    for activity in activities_from_file:
        # Separate out the activity attributes
        activity_attributes = activity.strip().split(' ')
        # Add this parsed activity to the list of activities
        activities.append((str(activity_attributes[0]), int(activity_attributes[1]),
                           int(activity_attributes[2]), int(activity_attributes[3])))

    return activities
