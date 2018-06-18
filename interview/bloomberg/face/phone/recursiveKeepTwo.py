"""
手机游戏题目：
例子1：AABBCCCCDD -> AABBDD
例子2：AABBCCCCBADD -> AABBBADD ->AAADD->D
就是把大于等于三个连续字母给去掉, 问最后剩的字符串
"""
class Solution(object):
	def keepTwo(self, s):
		count, res = 0, ""
		for i in range(len(s) + 1):
			if i != len(s) and (i == 0 or s[i] == s[i - 1]):
				count += 1
			else:
				if count < 3:
					res += "".join([s[i - 1]] * count)
				count = 1
		return res
	def recursiveKeepTwo(self, s):
		ss = self.keepTwo(s)
		return ss if s == ss else self.recursiveKeepTwo(ss)
s = Solution()
print s.recursiveKeepTwo("AABBCCCCBADD")