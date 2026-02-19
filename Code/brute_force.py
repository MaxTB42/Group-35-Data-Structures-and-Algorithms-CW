"""
This Python module houses the brute force approach to ECM1414 Data Structures
and Algorithms Coursework.
"""

from itertools import combinations

def generate_subset(activity_indices: tuple[int], size_of_subset: int) -> list[tuple]:
    """
    This function generates all subsets of a given size using the provided list of indices.

    ### The Idea:
    So that the activity data isn't duplicated many times, this function will generate all subsets
    (of a specified size) of indices, which range from 1 to n (number of activities). These indices
    can then be used to work out which activity belongs to which subset.
    """

    # Return the list containing the subsets of size "size_of_subset"
    return combinations(activity_indices, size_of_subset)

def find_optimal_solution(activity_list: list[tuple]) -> dict:
    """
    This function calls the generate_subset() function, then evaluates all returned subsets to
    determine which subset maximises the enjoyment value whilst adhering to the constraint
    of budget.
    """

    # Extract the total budget we have available
    available_budget = activity_list[0][2]

    # Initialise dictionary to hold optimal solution
    optimal_subset = {
        'subset_indices': (),
        'required_time': 0,
        'required_budget': 0,
        'total_enjoyment_value': 0
    }

    # Generate a list of integers ranging from 1 to n+1
    # n being number_of_activites
    # We start at 1 because the first element in the activity list is metadata
    activity_indices = range(1, activity_list[0] + 1)

    # Generate and evaluate all subsets
    for size_of_subset in range(1, activity_list[0] + 1):
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
                sum_of_time += activity_list[activity_index][1]
                sum_of_budget += activity_list[activity_index][2]
                sum_of_enjoyment_values += activity_list[activity_index][3]

            # Check if the total budget required for this subset is within the
            # available budget, and that the enjoyment value is larger than the current largest
            if (sum_of_enjoyment_values >= optimal_subset['total_enjoyment_value']
                and sum_of_budget <= available_budget):
                # Therefore we have found a new optimal subset, so update the dictionary
                optimal_subset['subset_indices'] = subset
                optimal_subset['required_time'] = sum_of_time
                optimal_subset['required_budget'] = sum_of_budget
                optimal_subset['total_enjoyment_value'] = sum_of_enjoyment_values

    # Return the optimal solution
    return optimal_subset
