#!/usr/bin/python
"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""

class Solution(object):
	def solveEquation(self, equation):
		"""
		:type equation: str
		:rtype: str
		"""
		def get(s):
			ss = map(lambda a: a if a !="-x" else "-1x", filter(lambda a: len(a) > 0, s.replace("-","+-").split("+")))
			x = sum(map(lambda a:int(a[:-1]) if len(a) > 1 else 1, filter(lambda a: "x" in a, ss)))
			nx  = sum(map(lambda a:int(a), filter(lambda a: "x" not in a, ss)))
			return (x, nx)
		l, r = equation.split("=")
		lx, lnx = get(l)
		rx, rnx = get(r)
		if lnx == rnx and lx == rx:
			return "Infinite solutions"
		elif lx == rx and lnx != rnx:
			return "No solution" 
		else:
			return "x=" + str((rnx - lnx) / (lx - rx)) 
s = Solution()
print s.solveEquation("2x=x")