"""
This mobule parses the input file, formatting the activities in
a way that is suitable for the algorithms.
"""

# Used to exit the program if file doesn't exist
import sys
# Used to access the input files in the Input_Files directory
from pathlib import Path

def file_input(input_file_name: str) -> list[tuple]:
    """
    This is the function that reads and parses the input file.

    ### Parameters:
     - `input_file_name` -> the name of the requested file as a string.
    
    ### Return Data Format:
     - A list of tupes is returned.
     - The first tuple contains 3 metadata elements: number of activities, available time, 
       and available budget.
     - Every subsequent tuple contains 4 elements about each activity: activity name,
       time required, budget required, and enjoyment value.
    """

    # Use Path to construct the path to the input file
    # Note: cwd = "current working directory"
    input_file_path = Path.cwd().parent / "Input_Files" / input_file_name

    # If the file doesn't exist, inform the user
    if Path.exists(input_file_path) is False:
        print(f"File '{input_file_name}' doesn't exist in the directory: '{input_file_path.parent}'.")
        # Exit the program
        sys.exit()

    # Initialise variables used for file parsing
    activities_from_file = []
    time_and_budget_line = ''
    number_of_activities = 0

    # Read the file contents
    with open(input_file_path, mode='r', encoding='utf-8') as activity_file:
        # Extract the number of activities and time/budget lines
        number_of_activities = int(activity_file.readline())
        time_and_budget_line = activity_file.readline()
        # Read the rest of the file and split into each activity line
        activities_from_file += activity_file.read().splitlines()

    # Extract the time and budget from line 2
    time_and_budget_separated = time_and_budget_line.strip().split(' ')
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
