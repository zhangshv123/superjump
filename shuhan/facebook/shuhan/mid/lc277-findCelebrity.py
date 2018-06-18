#!/usr/bin/python
class Solution(object):
	def findCelebrity(self, n):
		"""
		第一个for循环，从第0个人开始，如果k是第0个人认识的第一个人，说明1到k-1这些人0不认识，所以排除了名人的可能。按照此规则进行下去，最后candidate停在某一个位置，这个位置后面一定也没有名人，因为有的话，candidate会update等于它
		"""
		celebrity = 0
		for i in range(1,n):
			if knows(celebrity,i):
				celebrity = i
		
		for j in range(n):
			if celebrity != j and knows(celebrity,j) or not knows(j,celebrity):
				return -1
		
		return celebrity