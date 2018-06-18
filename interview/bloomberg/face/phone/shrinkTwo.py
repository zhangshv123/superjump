"""
压缩string, 比如： aabboooooooc -> aabbo#7c. 我问他是不是重复大于2就压缩，他说是。
然后如果后面在此出现相同的重复，还是需要重新考虑。
"""
class Solution(object):
	def shrinkTwo(self, s):
		count, res = 0, ""
		for i in range(len(s) + 1):
			if i != len(s) and (i == 0 or s[i] == s[i - 1]):
				count += 1
			else:
				if count < 3:
					res += "".join([s[i - 1]] * count)
				else:
					res += s[i - 1] + "#" + str(count)
				count = 1
		return res
s = Solution()
print s.shrinkTwo("AABBCCCCBADD")