import heapq
假设总共有k个list，每个list的最大长度是n
Time:knlog(k)因为每个element用一次
import heapq
def kMerge(arrs):
	h = []
	res = []
	p = [1]*len(arrs) #一个list来存每个arr进展到哪个idx了
	for i in range(len(arrs)):
		heapq.heappush(h, (arrs[i][0],i))
	
	while len(h) > 0:
		cur,idx = heapq.heappop(h)
		res.append(cur)
		if p[idx] < len(arrs[idx]):
			heapq.heappush(h, (arrs[idx][p[idx]],idx))
			p[idx] += 1
	return res

print kMerge([[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]])

print kMerge(4,[[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]])
1.merge2个复杂度多少？k个多少？
假设总共有k个list，每个list的最大长度是n
knlog(k)
这个算法每个元素要读取一次，即是k*n次，然后每次读取元素要把新元素插入堆中要logk的复杂度，所以总时间复杂度是O(nklogk)。
空间复杂度是堆的大小，即为O(k)
2.比较优缺点 为什么 kway merge 比 2way merge 好
merge2: 浪费临时存储空间
每次中间的临时都要存储到disk里面去，然后还要读出来，就慢很多
kmerge:节省空间
3.k个array 在k个文件里，每个文件4G，memery2个G（外部排序）
kmerge,每次merge 2G
每个文件读2G/K，好要留点给排好序的部分

		
	
	
	
	
	
	