#!/usr/bin/python
class Solution(object):
	def addBinary(self, a, b):
		"""
		和一般的加法一样的
		time:O(len(a)+len(b))
		"""
		res = ""
		sum,carry = 0,0
		i,j = len(a)-1,len(b)-1
		while i >= 0 or j >= 0:
			sum = carry
			if i>=0:
				sum+=int(a[i])
				i-=1
			if j >=0:
				sum+=int(b[j])
				j-=1
			carry = sum/2
			cur = sum%2
			res += str(cur)
		if carry != 0:
			res += str(carry)
		return res[::-1]
