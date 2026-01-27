from itertools import combinations

def generate_subsets(number_of_activities: int) -> list[tuple]:
    """
    This function generates all possible subsets of a given list of activity indices.

    ##### The Idea:
    Since the activity dictionary's keys are indices, this function will generate all possible
    subsets of indices, which range from 0 to n-1. These indices can then be used to work out
    which activity belongs to which subset. This approach avoids having to duplicate the
    activity data many times.
    """

    # Generate a list of integers ranging from 0 to n-1
    # n being number_of_activites
    activity_indices = range(number_of_activities)

    # Initialise a list to hold all the subsets
    subsets = []

    # Iterate to create combinations of increasing size
    for i in range(number_of_activities + 1):
      subsets += list(combinations(activity_indices, i))
    
    # Return the list of all possible subsets
    return subsets

# Test
print(generate_subsets(3))
