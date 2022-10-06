# Note: This reward function may not work exactly the same if
# copied into a different setup due to different training execution.

def reward_function(params):
	
	# Example of reward function that incentivizes the car to go at
	# top speed at each step
    # Function header & variables
	# Read input parameters
	speed = params['speed']
	is_offtrack = params['is_offtrack']
	# Speed threshold, change the number based on 
	# your action space setting
	TOP_SPEED = 2.0 
	# Give a zero reward by default
	reward = 0
	# Give higher reward if the car is going at top speed
	if speed == TOP_SPEED:
		reward = 1.0
	# Give a negative reward if the car goes offtrack
	if is_offtrack:
		reward = -1
    return float(reward)