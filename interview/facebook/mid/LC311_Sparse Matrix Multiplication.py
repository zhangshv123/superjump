"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
"""
top solution, just use naive 3 for loop
"""

YY的follow up:
不管input是leetcode的矩阵,还是（x,y,val）代表所有非0的节点，
都转化成邻接表 adjact list
https://www.cnblogs.com/XMU-hcq/p/6065057.html
[[(1,1)],[],[]]
对于A：
for i in range(n):
	adj[i] = []
for i in range(n):
	for j in range(n):
		if a[i][j] != 0:   
			adjA[j].append((i, a[i][j])) i是a的第i行，
对于B：
for i in range(n):
	for j in range(n):
		if b[i][j] != 0:
			adjB[i].append((j, b[i][j]))  j是b的第j行

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, nB = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(nB)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(nB):
                        if B[j][k] != 0:
                            C[i][k] += A[i][j] * B[j][k]
        return C


"""
not helpful, even worse time complexity
"""
class Solution(object):
	def rotate_matrix(self, A):
		row, col = len(A), len(A[0])
		rot = [ [0 for _ in range(row)] for _ in range(col)]
		for i in range(row):
			for j in range(col):
				rot[j][i] = A[i][j]
		return rot

	def shrink_matrix(self, A):
		map_A = []
		for row in A:
			map_row = {}
			for i, item in enumerate(row):
				if item != 0:
					map_row[i] = item
			map_A.append(map_row)
		return map_A
	def intersection(self, list_A, list_B):
		return filter(lambda a: a in list_B, list_A)
	def multiply(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		"""
		map_A = self.shrink_matrix(A)
		map_B = self.shrink_matrix(self.rotate_matrix(B))
		len_i, len_k, len_j = len(A), len(A[0]), len(B[0])
		C = [ [0 for _ in range(len_j)] for _ in range(len_i)]
		for i in range(len_i):
			for j in range(len_j):
				for k in self.intersection(map_A[i].keys(), map_B[j].keys()):
					C[i][j] += map_A[i][k] * map_B[j][k]
		return C