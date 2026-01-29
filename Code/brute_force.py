"""
This Python module houses the brute force approach to ECM1414 Data Structures
and Algorithms Coursework.
"""

from itertools import combinations
from pathlib import Path
import time
from file_input import file_input

def generate_subset(activity_indices: tuple[int], size_of_subset: int) -> list[tuple]:
    """
    This function generates a list of activity indices using the number of activities provided
    and then generates all subsets of a given size using this list of indices.

    ### The Idea:
    Since the activity dictionary's keys are indices, this function will generate all subsets
    (of a specified size) of indices, which range from 3 to n+2. These indices can then be used
    to work out which activity belongs to which subset. This approach avoids having to duplicate the
    activity data many times.
    """

    # Return the list containing the subsets of size "size_of_subset"
    return combinations(activity_indices, size_of_subset)

def find_optimal_solution(activity_dict: dict) -> dict:
    """
    This function calls the generate_subset() function, then evaluates all returned subsets to
    determine which subset maximises the enjoyment value whilst adhering to the constraint
    of budget.
    """

    # Extract the total budget we have available
    available_budget = activity_dict[2]
    available_time = activity_dict[1]

    # Initialise dictionary to hold optimal solution
    optimal_subset = {
        'subset_indices': (),
        'required_time': 0,
        'required_budget': 0,
        'total_enjoyment_value': 0
    }

    # Generate a list of integers ranging from 3 to n+2
    # n being number_of_activites
    # We start at 3 because there are 3 elements in the activity dictionary that are metadata
    activity_indices = range(3, activity_dict[0] + 3)

    # Iterate to generate and evaluate all subsets
    for size_of_subset in range(1, activity_dict[0] + 1):
        # Generate the subsets of size "size_of_subset"
        subsets = generate_subset(activity_indices, size_of_subset)

        # Iterate through and evaluate each subset
        for subset in subsets:
            # Initialise the sum of budget, time and enjoyment value trackers
            sum_of_budget = 0
            sum_of_time = 0
            sum_of_enjoyment_values = 0

            # Iterate through each activity index in the subset
            for activity_index in subset:
                # Add this activity's budget and enjoyment value to the counters
                sum_of_time += activity_dict[activity_index][1]
                sum_of_budget += activity_dict[activity_index][2]
                sum_of_enjoyment_values += activity_dict[activity_index][3]

            # Check if the total budget required for this subset is within the available budget
            # and that the enjoyment value is larger than the current largest
            if (sum_of_enjoyment_values >= optimal_subset['total_enjoyment_value']
                and sum_of_budget <= available_budget
                and sum_of_time <= available_time):
                # Therefore we have found a new optimal subset, so update the dictionary
                optimal_subset = {
                'subset_indices': subset,
                'required_time': sum_of_time,
                'required_budget': sum_of_budget,
                'total_enjoyment_value': sum_of_enjoyment_values
                }

    # Return the optimal solution
    return optimal_subset

# Test Section
# Set up the file path to the input file
file_path = Path(__file__).parent.parent / 'Input_Files' / 'input_10.txt'
activity_dictionary = file_input(file_path)

# Start the timer
start_time = time.time()

# Start the brute force algorithm
optimal_solution = find_optimal_solution(activity_dictionary)

# End the timer
end_time = time.time()

# Output the optimal solution
print(optimal_solution)

# Output the optimal selection of activities
for index in enumerate(optimal_solution['subset_indices']):
    print(f"Activity {index[0] + 1}: {activity_dictionary[index[1]]}")

# Output the execution time
print(f"\n=== Brute Force Algorithm took {end_time - start_time} seconds ===")