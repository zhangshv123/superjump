#论坛上有人称之为二分解法，但是博主怎么觉得不是呢，虽然样子很像，但是并没有折半的操作啊。这里用a和b代表了左右两个范围，分别为0和c的平方根，然后while循环遍历，如果a*a + b*b刚好等于c，那么返回true；如果小于c，则a增大1；反之如果大于c，则b自减1
import math
class Solution(object):
	def judgeSquareSum(self, c):
		"""
		:type c: int
		:rtype: bool
		"""
		a, b = 0, int(math.sqrt(c))
		while a <= b:
			if a*a + b*b == c:
				return True
			elif a*a + b*b < c:
				a += 1
			else:
				b -= 1
		return False