#!/usr/bin/python
class Solution(object):
	def SparseMatrixMultiplication(self, A, B):
		"""
		:type A: List[List[int]]
		:type B: List[List[int]]
		:rtype: List[List[int]]
		time: O(rA*cA*cB)
		这道题让我们实现稀疏矩阵相乘，稀疏矩阵的特点是矩阵中绝大多数的元素为0，而相乘的结果是还应该是稀疏矩阵，即还是大多数元素为0，那么我们使用传统的矩阵相乘的算法肯定会处理大量的0乘0的无用功，所以我们需要适当的优化算法，使其可以顺利通过OJ，我们知道一个 i x k 的矩阵A乘以一个 k x j 的矩阵B会得到一个 i x j 大小的矩阵C，那么我们来看结果矩阵中的某个元素C[i][j]是怎么来的，起始是A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]，那么为了不重复计算0乘0，我们首先遍历A数组，要确保A[i][k]不为0，才继续计算，然后我们遍历B矩阵的第k行，如果B[K][J]不为0，我们累加结果矩阵res[i][j] += A[i][k] * B[k][j]; 这样我们就能高效的算出稀疏矩阵的乘法
		"""
		rA,cA,cB = len(A),len(A[0]),len(B[0])
		C = [[0 for _ in range(cB)] for _ in range(rA)]
		for i in range(rA):
			for k in range(cA):
				if A[i][k] != 0:
					for j in range(cB):
						if B[k][j]!= 0:
							C[i][j] +=A[i][k]*B[k][j]
		
		return C
