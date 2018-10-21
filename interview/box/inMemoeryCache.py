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
