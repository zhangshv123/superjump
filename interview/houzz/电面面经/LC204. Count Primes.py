思路参考链接：
https://blog.csdn.net/github_39261590/article/details/73864039
class Solution:
	# @param {integer} n
	# @return {integer}
	def countPrimes(self, n):
		isPrime = [True] * max(n, 2)
		isPrime[0], isPrime[1] = False, False
		x = 2
		while x * x < n:
			if isPrime[x]:
				p = x * x
				while p < n:
					isPrime[p] = False
					p += x
			x += 1
		return sum(isPrime)