"""
This Python module houses the dynamic programming method to ECM1414 Data Structures
and Algorithms Coursework using the cost as a limitation.
"""

def dynamic_subsets(activity_list: list[tuple]) -> dict:
    """
    This function generates all possible subsets of a given
    list using dynamic programming algorithm.
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

    #Initiates the Dynamic Programming table
    dp_table = [0] * (av_budget + 1)

    #Adds each activity to the DP table
    for act in activities:
        act_cost = act[2]
        act_enjoy = act[3]
        for i in range(av_budget, act_cost-1, -1):
            dp_table[i] = max(dp_table[i], dp_table[i - act_cost] + act_enjoy)

    subsets = []
    budget = av_budget
    total_time = 0
    required_budget = 0
    total_enjoy = 0

    #Generates each subset of activities, ensuring budget doesn't exceed
    for i in range(num_activities-1,-1,-1):
        act_cost = activities[i][2]
        act_enjoy = activities[i][3]
        act_time = activities[i][1]

        if budget >= act_cost and dp_table[budget] == dp_table[budget - act_cost] + act_enjoy:
            subsets.append(activities[i])
            budget = budget - act_cost
            total_time += act_time
            required_budget += act_cost
            total_enjoy += act_enjoy

    optimal_subset['subset'] = subsets
    optimal_subset['time_used'] = total_time
    optimal_subset['budget_used'] = required_budget
    optimal_subset['total_enjoyment_value'] = total_enjoy

    return optimal_subset
