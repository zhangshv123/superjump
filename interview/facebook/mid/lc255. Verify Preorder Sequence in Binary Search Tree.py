请参考：
https://segmentfault.com/a/1190000003874375
import sys
class Solution(object):
	def verifyPreorder(self, preorder):
		stk = []
		minValue = -sys.maxint
		for num in preorder:
			if num < minValue:
				return False
			while len(stk) > 0 and num > stk[-1]:
				minValue = stk.pop()
			stk.append(num)
		return True
		
	
	