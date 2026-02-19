"""
This is the main entry point for the coursework.
It uses the two algorihtms to produce the optimal subset of activities.
It then produces a human readable output of the optimal solution.
"""

# Used for the command line argument "input_file_name"
import sys
# Used to access the input files in the Input_Files directory
# Used to manipulate the path to the input file
from pathlib import Path

# Extract the file name form the terminal input
input_file_name = sys.argv[1]

# Use Path to construct the path to the input file
input_file_path = Path.cwd().parent / "Input_Files" / input_file_name

# If the file doesn't exist, inform the user
if Path.exists(input_file_path) is False:
    print(f"File '{input_file_name}' doesn't exist in path: '{input_file_path}'!")
    # Exit the program
    quit()

# Output the title
print("========================================")
print("Event Planner - Results")
print("========================================")

# Only run this program if called directly
if __name__ == "__main__":
    # Parse the file contents
    with open(input_file_path, 'r', encoding='utf8') as input_file:
        # Initialise a list to hold all the activities and metadata
        activities = []

        # Activity structure:
        # index 0: (number_of_activities, available_time, available_budget)
        # index 1: (activity_name, activity_time, activity_budget, activity_enjoyment_value)
        # index 2: ...

        # Read the metadata
        # Convert number of activities to an integer
        number_of_activities = int(input_file.readline())

        # Parse the second line containing the constraints: time and budget
        line_2_split = input_file.readline().strip().split(' ')
        available_time = int(line_2_split[0])
        available_budget = int(line_2_split[1])

        # Add metadata to activity list
        activities.append((number_of_activities, available_time, available_budget))

        # Iterate through the rest of the file, parsing each activity
        for i in range(number_of_activities):
            # Read the activity line
            activity = input_file.readline()
            # Strip and split the line
            line_split = activity.strip().split(' ')
            # Add this activity data to the activity list
            activities.append((line_split[0], int(line_split[1]),
                               int(line_split[2]), int(line_split[3])))

        print(activities)
