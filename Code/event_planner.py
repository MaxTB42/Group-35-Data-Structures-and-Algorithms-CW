"""
This is the main entry point for the coursework.
It uses the two algorihtms to produce the optimal subset of activities.
It then produces a human readable output of the optimal solution.
"""

# Used for the command line argument "file_name"
import sys
# Used to measure the execution time of the algorithms
from time import time
# Used to parse the input file
from file_input import file_input
# Used to access the brute force algorithm
from brute_force import find_optimal_solution
# Used to access the dynamic programming algorithm
from dynamic_method import dynamic_subsets

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
    print("========================================\n")

    # Output file name and matadata
    print(f"Input File: {file_name}")
    print(f"Available Time: {activities[0][1]} {"hour" if activities[0][1] == 1 else "hours"}")
    print(f"Available Budget: £{activities[0][2]}\n")


    # === BRUTE FORCE SECTION ===
    # Start the execution timer for the brute force algorithm
    bf_start_time = time()
    # Call the brute force algorithm to calculate the optimal solution
    brute_force_optimal_sol = find_optimal_solution(activities)
    # End the timer
    bf_execution_time = time() - bf_start_time
    # Output algorithm title
    print("--- BRUTE FORCE ALGORITHM ---")
    # Output the solution
    print("Selected Activities:")
    # Iterate through each selected activity
    for activity_index in brute_force_optimal_sol['subset_indices']:
        # Extract the activity
        activity = activities[activity_index]
        # Output the choosen activity
        print(f"  - {activity[0]} ({activity[1]} {"hour" if activity[1] == 1 else "hours"}, "\
              f"£{activity[2]}, enjoyment {activity[3]})")
    # Output the total enjoyment, time and cost
    print(f"\nTotal Enjoyment: {brute_force_optimal_sol["total_enjoyment_value"]}")
    print(f"Total Time Used: {brute_force_optimal_sol["time_used"]} hours")
    print(f"Total Cost: £{brute_force_optimal_sol["budget_used"]}\n")
    # Output the execution time
    print(f"Execution Time: {bf_execution_time:.6f} seconds")


    # === DYNAMIC SECTION ===
    # Start the execution timer for the dynamic programming algorithm
    dp_start_time = time()
    # Call the dynamic programming algorithm to calculate the optimal solution
    dynamic_programming_optimal_sol = dynamic_subsets(activities)
    # End the timer
    dp_execution_time = time() - dp_start_time
    # Output algorithm title
    print("\n--- DYNAMIC PROGRAMMING ALGORITHM ---")
    # Output the solution
    print("Selected Activities:")
    # Iterate through each selected activity
    for activity in dynamic_programming_optimal_sol['subset']:
        # Output the choosen activity
        print(f"  - {activity[0]} ({activity[1]} {"hour" if activity[1] == 1 else "hours"}, "\
              f"£{activity[2]}, enjoyment {activity[3]})")
    # Output the total enjoyment, time and cost
    print(f"\nTotal Enjoyment: {dynamic_programming_optimal_sol["total_enjoyment_value"]}")
    print(f"Total Time Used: {dynamic_programming_optimal_sol["time_used"]} hours")
    print(f"Total Cost: £{dynamic_programming_optimal_sol["budget_used"]}\n")
    # Output the execution time
    print(f"Execution Time: {dp_execution_time:.6f} seconds")

    print("\n========================================")
