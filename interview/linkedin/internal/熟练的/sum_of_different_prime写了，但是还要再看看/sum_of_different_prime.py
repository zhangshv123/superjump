class Solution:
	def generatePrimes(self, n):
		primeArray = [True] * max(n, 2)
		primeArray[0], primeArray[1] = False, False
		x = 2
		while x * x < n:
			if primeArray[x]:
				p = x * x
				while p < n:
					primeArray[p] = False
					p += x
			x += 1
		new_res = []
		for i in range(len(primeArray)):
			if primeArray[i]:
				new_res.append(i)
		return new_res
	
	def count_ways(self, n, k):
		primeArray = self.generatePrimes(n)
		print primeArray
		dp = [[0 for i in range(k+1)]for j in range(n+1)]
		dp[0][0] = 1
		for p in range(len(primeArray)):
			for i in range(n, p-1, -1):
				for j in range(1,k+1):
					dp[i][j] += dp[i - primeArray[p]][j-1]
		return dp[n][k]

s = Solution()
print s.count_ways(5, 2)