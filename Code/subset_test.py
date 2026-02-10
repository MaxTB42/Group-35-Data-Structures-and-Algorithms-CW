"""Test python file"""

from itertools import combinations
from file_input_new import file_input

def generate_subset_old(activity_indices: tuple[int], size_of_subset: int) -> list[tuple]:
    """
    This function generates all subsets of a given size using the provided list of indices.

    ### The Idea:
    Since the activity dictionary's keys are indices, this function will generate all subsets
    (of a specified size) of indices, which range from 3 to n+2. These indices can then be used
    to work out which activity belongs to which subset. This approach avoids having to duplicate the
    activity data many times.
    """

    # Create a group of elements of size "size_of_subset" - 1
    group_start = 0
    group_end = size_of_subset - 2 if size_of_subset - 2 > 0 else 0

    # Create a list to store the subsets
    subsets = []

    # Iterate, shifting the group up by one element each iteration
    for i in range(len(activity_indices)):
        # Store the current group
        current_group = list(activity_indices[group_start:group_end+1])

        # Iterate, adding every other element to the group to form the subset
        for other_element in activity_indices[group_end + 1:len(activity_indices)]:
            # Add this new subset to the list
            current_group.append(other_element)
            subsets.append(tuple(current_group))
            current_group = list(activity_indices[group_start:group_end+1])

        # Shift the group up one element
        group_start += 1
        group_end += 1

    # Return the list containing the subsets of size "size_of_subset"
    return subsets


def generate_subset(activity_indices: tuple[int], size_of_subset: int) -> list[tuple]:
    """
    This function generates all subsets of a given size using the provided list of indices.

    ### The Idea:
    To save duplicating the activity data multiple times, this function will generate all subsets
    (of a specified size) of indices for each activity, which range from 1 to n. These indices can
    then be used to work out which activity belongs to which subset. This approach avoids having
    to duplicate the activity data many times.
    """

    # Initialise a list to hold the subsets
    subsets = []

    # Base case: if subset size is 1, return a list of individual elements.
    if size_of_subset == 1:
        # Loop through each element
        for element in activity_indices:
            # Add this element to the list of subsets
            subsets.append([element])
        return subsets

    # Recursive section:
    # Calculate all the subsets of size n-1
    subsets = generate_subset(activity_indices, size_of_subset - 1)

    # Iterate through the activity index list and add each element to the subset
    for element in activity_indices:
        for i in range(len(subsets)):
            # Ensure the current element isn't already in the subset
            if not (element in subsets[i]):
                subsets[i].append(element)

    return subsets


# Parse the activity file
activities = \
file_input(r"C:\.dev\Group-35-Data-Structures-and-Algorithms-CW\Input_Files\input_small.txt")

# Generate a list of activity indices
activity_indices = range(len(activities) - 1)

# Iterate through and generate all subsets
for size in range(1, len(activities)):
    print(f"Size = {size}")
    # Use itertools.combinations to generate all subsets of a given size
    print("Library:", list(combinations(activity_indices, size)))
    print("Custom: ", list(generate_subset(activity_indices, size)))
    print()
