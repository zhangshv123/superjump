解题思路：
请参考
http://tinyurl.com/y9jkbglj
class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		if denominator == 0:
			return 0
		negative = numerator*denominator < 0
		numerator = abs(numerator)
		denominator = abs(denominator)
		loopArr = []
		d = dict()
		res = None
		cnt = 0
		while True:
			cnt += 1
			inte = numerator/denominator
			left = (numerator%denominator)*10
			loopArr.append(str(inte))
			numerator = left
			if left == 0:
				if len(loopArr) > 1:
					res =loopArr[0] + "."+ "".join(loopArr[1:])
					break
				else:
					res = loopArr[0]
					break
			if left in d:
				start = d[left]
				res = str(loopArr[0]) + "." + "".join(loopArr[1:start]) + "(" + "".join(loopArr[start:]) + ")"
				break
			else:
				d[left] = cnt
		if negative:
			res  = "-"+res
		return res

s = Solution()
print s.fractionToDecimal(-2,-6)
				
		
			
	