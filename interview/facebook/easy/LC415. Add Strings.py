class Solution(object):
	def addStrings(self, num1, num2):
		i, j = len(num1) - 1, len(num2) - 1
		res = ""
		carry = 0
		while i >= 0 or j >=0:
			while i >= 0 and j >=0:
				total = int(num1[i]) + int(num2[j]) + carry
				carry = total/10
				res = str(total%10) + res 
				i -= 1
				j -= 1
			while i >= 0:
				total = int(num1[i]) + carry
				carry = total/10
				res = str(total%10) + res
				i-= 1
			while j >= 0:
				total = int(num2[j]) + carry
				carry = total/10
				res = str(total%10) + res
				j -= 1
			if carry != 0:
				res = str(carry) + res
		return res

s = Solution()
print s.addStrings("45", "1555")
				
			
			
			
			