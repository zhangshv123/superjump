class Solution(object):
	def findStrobogrammatic(self, n):
		d = {"1":"1","6":"9","8":"8","9":"6","0":"0"}
		if n == 0:
			return [""]
		if n == 1:
			return ["0","1","8"]
		res = []
		self.dfs(n/2,[],res,d, n)
		for i, item in enumerate(res):
			for j in range(len(item)-1, -1, -1):
				item.append(d[item[j]])
				res[i] = "".join(item)	
		if n%2 == 0:
			return res
		else:
			new_res = []
			for key in ["1","8","0"]:
				for i, item in enumerate(res):
					idx = len(item)/2
					new_item = item[:idx] + key + item[idx:]
					new_res.append(new_item)
			return new_res
			
	def dfs(self, left, path, res, d, n):
		if left == 0:
			res.append(path[:])
			return
		
		for key in d.keys():
			if left == n/2 and key == "0":
				continue
			path.append(key)
			self.dfs(left-1, path, res, d, n)
			path.pop()
	
s = Solution()
print s.findStrobogrammatic(3)
print s.findStrobogrammatic(1)
print s.findStrobogrammatic(6)
		