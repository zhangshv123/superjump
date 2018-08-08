一个直观的思路是先统计每个字符的数量，然后将这些字符连同频率放入一个优先队列中，再取出来即可．这种时间复杂度为O(n) + O(m log m)，其中n为字符串长度，m为不同字符的个数，在最坏情况下时间复杂度为O(n log n)，即所有字符都不一样．其实我们还有一种可以优化的方法，在统计完字符频率之后利用类似与计数排序的方法，开一个n+1长度大小的数组，将不同的频率字符放到频率的索引处．然后从高到低取得所有字符串．这种方法的好处是在最环情况下依然可以保证时间复杂度为O(n)．

from collections import defaultdict
import heapq
class Solution(object):
	def frequencySort(self, s):
		res = ""
		h = []
		d = defaultdict(int)
		for c in s:
			d[c] += 1
		arr = [""]*(len(s)+1)
		for key in d.keys():
			arr[d[key]] += key
		for i in range(len(arr)-1, 0, -1):
			if arr[i] != "":
				for c in arr[i]:
					res += i*c
		return res
		
#heap的版本 O(n) + O(m log m)
from collections import defaultdict
import heapq
class Solution(object):
	def frequencySort(self, s):
		res = ""
		h = []
		d = defaultdict(int)
		for c in s:
			d[c] += 1
		for key in d.keys():
			heapq.heappush(h, (-d[key],key))
		while len(h) > 0:
			tup = heapq.heappop(h)
			for i in range(-tup[0]):
				res += tup[1]
		return res
        
s = Solution()
print s.frequencySort("tree")
		