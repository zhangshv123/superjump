from collections import defaultdict
class Solution(object):
	def inMemoeryCache(self):
		cache = defaultdict(str)
		cacheInverted = defaultdict(int)
		cur = defaultdict(str)
		curInverted = defaultdict(int)
		with open("/Users/shuhanzhang/Documents/aa.txt", "rb") as fin: 
			for line in fin:
				if line.startswith("set"):
					arr = line.split("(")[1].split(")")[0].split(",")
					cache[arr[0]] = arr[1]
					cacheInverted[arr[1]] += 1
					print arr
				elif line.startswith("get"):
					key = line.split("(")[1].split(")")[0]
					print cache[key]
				elif line.startswith("count"):
					target = line.split("(")[1].split(")")[0]
					print cacheInverted[target]
				elif line.startswith("delete"):
					key = line.split("(")[1].split(")")[0]
					cacheInverted[cache[key]] -= 1
					del cache[key]
					print "deleted" + str(key)
				elif line.startswith("begin"):
					continue
				elif line.startswith("commit"):
					cur = cache.copy()
					curInverted = cacheInverted.copy()
					print "commit!"
				elif line.startswith("rollback"):
					cache = cur
					cacheInverted = curInverted
		return "end"
					
s = Solution()
print s.inMemoeryCache()

方法2：
from collections import defaultdict
class Solution:
	def tryCache(self):
		cache = defaultdict(str)
		cacheInverted = defaultdict(int)
		stack = []
		while (True):
			line = raw_input()
			if line.startswith("end"):
				return
			self.helper(line, cache, cacheInverted, stack)
			
	
	def helper(self, line, cache, cacheInverted, stack, rollback_only=False):
		if line.startswith("set"):
			arr = line.split()
			if arr[1] in cache:
				target = cache[arr[1]]
				cacheInverted[target] -= 1
			if len(stack) > 0 and not rollback_only:
				if arr[1] in cache:
					stack[-1].append("set " + arr[1] + " " + target)
				else:
					stack[-1].append("delete " + arr[1])
			cache[arr[1]] = arr[2]
			cacheInverted[arr[2]] += 1
		elif line.startswith("get"):
			key = line.split()[1]
			if key not in cache:
				print "NULL"
			else:
				print cache[key]
		elif line.startswith("count"):
			target = line.split()[1]
			print cacheInverted[target]
		elif line.startswith("delete"):
			arr = line.split()
			target = cache[arr[1]]
			cacheInverted[target] -= 1
			if len(stack) > 0 and not rollback_only:
				stack[-1].append("set " + arr[1] + " " + target)
			del cache[arr[1]]
			print "deleted " + str(arr[1])
		elif line.startswith("begin"):
			stack.append([])
		elif line.startswith("commit"):
			if len(stack) > 0:
				stack[:] = []
				return
			print "no transaction"
		elif line.startswith("rollback"):
			if len(stack) == 0:
				print "no transaction"
				return
			cur = stack.pop()
			for i in range(len(cur)-1, -1, -1):
				self.helper(cur[i], cache, cacheInverted, stack, rollback_only=True)

s = Solution()
s.tryCache()
		
				
			
		
