from collections import defaultdict
class Solution(object):
	def findDuplicate(self, paths):
		"""
		:type paths: List[str]
		:rtype: List[List[str]]
		"""
		store = defaultdict(list)
		for path in paths:
			splitted_path = path.split(" ")
			for rest in splitted_path[1:]:
				filename, content = rest.split("(")
				store[content].append(splitted_path[0] + "/" + filename)
		return [value for value in store.values() if len(value) > 1]
		
s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
