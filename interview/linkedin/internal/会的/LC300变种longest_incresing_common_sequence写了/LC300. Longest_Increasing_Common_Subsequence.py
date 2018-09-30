思路：
dp[i][j] 表示以a[i]结尾，b[0-j]之间某个数作为结尾的最长LCIS
dp 方程：
1) a[i] == b[j]
dp[i][j] = max(dp[0][j-1].....dp[i-1][j-1]) and a[i‘] < a[i]
2) 如果不相等
dp[i][j] = dp[i][j-1]
最后要找的答案就是dp[k][len(b)-1],所以用个max的变量存起来就好了！
from collections import defaultdict
class Solution(object):
	def lengthOfLCIS(self, list1, list2):
		l1, l2 = len(list1), len(list2)
		dp = [[0 for j in range(l2)] for i in range(l1)]
		if list1[0] == list2[0]:
			dp[0][0] = 1
		for j in range(1, l2):
			if list1[0] == list2[j]:
				dp[0][j] = 1
			else:
				dp[0][j] = dp[0][j-1]
		for i in range(1,l1):
			if list1[i] == list2[0]:
				dp[i][0] = 1
		for i in range(1, l1):
			for j in range(1, l2):
				if list1[i] == list2[j]:
					max_v = 0
					for k in range(i):
						if list1[k] < list1[i]:
							max_v = max(max_v, dp[k][j-1])
					dp[i][j] = max_v + 1
				else:
					dp[i][j] = dp[i][j-1]
		res = 0
		for k in range(l1):
			res = max(res, dp[k][l2-1])
		return res
s = Solution()
print s.lengthOfLCIS([11,2,9,8,12,7], [11,5,2,8,9,12])
print s.lengthOfLCIS([11,2,9,8], [11,5,2,8,9,12])