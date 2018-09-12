def getHighestReward(matrix):
	row, col = len(matrix), len(matrix[0])
	reward = [[0 for i in range(col)] for j in range(row)]
	reward[0][0] = matrix[0][0]
	for i in range(1,row):
		reward[i][0] = reward[i-1][0] + matrix[i][0]
	for j in range(1,col):
		reward[0][j] = reward[0][j-1] + matrix[0][j]
	
	for i in range(1,row):
		for j in range(1,col):
			reward[i][j] = max(reward[i-1][j], reward[i][j-1]) +  matrix[i][j]
	
	return reward[-1][-1]

print getHighestReward([[2,4,3],[3,-3,0],[5,-6,4]])