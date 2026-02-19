"""
This is the main entry point for the coursework.
It uses the two algorihtms to produce the optimal subset of activities.
It then produces a human readable output of the optimal solution.
"""

# Used for the command line argument "file_name"
import sys
# Used to parse the input file
from file_input import file_input
# Used to access the brute force algorithm
from brute_force import find_optimal_solution
# Used to access the dynamic programming algorithm


# Only run this program if executed directly
if __name__ == "__main__":
    # Check if the user has entered a file name
    if len(sys.argv) <= 1:
        # Inform the user that they haven't inputted a file name
        print("Please provide a file name: e.g. 'input_small.txt'.")
        # Exit the program
        sys.exit()

    # Extract the file name form the terminal input
    file_name = sys.argv[1]

    # Call the file_input function to parse the file
    activities = file_input(file_name)

    # Output the title
    print("========================================")
    print("Event Planner - Results")
    print("========================================")

    print(activities)
