# http://www.cnblogs.com/grandyang/p/5200919.html
class Solution(object):
	def findStrobogrammatic(self, n):
		return self.find(n,n)
	
	def find(self, m, n):
		if m == 0:
			return [""]
		
		if m == 1:
			return ["0", "1", "8"]
		
		t = self.find(m-2, n)
		res = []
		for a in t:
			if m != n:
			res.append("0" + a + "0")
			res.append("1" + a + "1")
			res.append("6" + a + "9")
			res.append("8" + a + "8")
			res.append("9" + a + "6")
		
		return res
	
s = Solution()
print s.findStrobogrammatic(3)
print s.findStrobogrammatic(1)
print s.findStrobogrammatic(6)
		