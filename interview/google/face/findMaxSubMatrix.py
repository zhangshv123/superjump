题目：
给一个matrix（N*N）,找出里面所有k*k的submatrix的最大值
例子：
| 1  2  3 |
| 4  5  6 |  k = 2   得到   |4  6|
| 7  8  9 |                 |8  9|
dp[i][j][k] 表示 以 matrix[i][j]为右下角，边长为K的矩阵
def findMaxSubMatrix(matrix, k):
	N = len(matrix)
	dp = [[[None for i in range(k)]for j in range(N)]for m in range(N)]
	res = []
	
	for m in range(k):
		for i in range(N):
			for j in range(N):
				if m == 0:
					dp[i][j][m] = matrix[i][j]
				else:
					if i >=m and j >= m:
						dp[i][j][m] = max(dp[i-1][j-1][m-1],dp[i-1][j][m-1],dp[i][j-1][m-1],dp[i][j][m-1])
						if m == k-1:
							res.append(dp[i][j][k-1])
	
	return res

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix = [
 [ 1, 2],
 [ 4, 5]
]

matrix = [
 [ 1, 2, 3, 4],
 [ 4, 5, 6, 7],
 [ 6, 7, 8, 9],
 [ 7, 8, 9, 10]
]



print findMaxMatrix(matrix, 2)
	
				
				