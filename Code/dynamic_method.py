"""
This Python module houses the dynamic programming method to ECM1414 Data Structures
and Algorithms Coursework using the cost as a limitation.
It utilises a dynamic programming table to store results
previously executed to speed up computation time
"""

def dynamic_subsets(activity_list: list[tuple]) -> dict:
    """
    This function generates all possible subsets of a given
    list using dynamic programming algorithm. Then it generates
    the most optimal solution, whilst keeping to budget constraints.
    """
    #Sets initial values
    av_budget = activity_list[0][2]
    activities = activity_list[1:]
    num_activities = activity_list[0][0]

    # Create a dictionary to hold optimal solution
    optimal_subset = {
        'subset': (),
        'time_used': 0,
        'budget_used': 0,
        'total_enjoyment_value': 0
    }

    #Initiates the 2D Dynamic Programming table
    #Rows are 0 to num_activities
    #Columns represents budget, 0 to av_budget
    dp_table = []
    for i in range(num_activities + 1):
        row = [0] * (av_budget + 1) #Starts each value with a 0
        dp_table.append(row)

    #Adds each activity to the DP table
    for t in range(1, num_activities+1):
        act_cost = activities[t-1][2]
        act_enjoy = activities[t-1][3]

        for i in range(av_budget + 1):
            if act_cost <= i: #Add new activity and set to max enjoyment
                dp_table[t][i] = max(dp_table[t-1][i], dp_table[t-1][i - act_cost] + act_enjoy)
            else: #Exclude activity and copy previous result
                dp_table[t][i] = dp_table[t-1][i]

    #Initialises values for backtracking
    subsets = []
    budget = av_budget
    total_time = 0
    required_budget = 0
    total_enjoy = 0

    for i in range(num_activities, 0,-1):
        act_cost = activities[i-1][2]
        act_enjoy = activities[i-1][3]
        act_time = activities[i-1][1]

        #Checking if activities are optimal and update values
        if budget >= act_cost and dp_table[i][budget] != dp_table[i-1][budget]:
            subsets.append(activities[i-1])
            budget = budget - act_cost
            total_time += act_time
            required_budget += act_cost
            total_enjoy += act_enjoy

    #Stores optimal results in dictionary
    optimal_subset['subset'] = subsets
    optimal_subset['time_used'] = total_time
    optimal_subset['budget_used'] = required_budget
    optimal_subset['total_enjoyment_value'] = total_enjoy

    return optimal_subset
