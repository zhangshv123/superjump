import heapq
n个array,每个array有k个num
Time:0(kn)因为每个element用一次
def kMerge(k,arrs):
	h = []
	count = k
	res = []
	for i in range(len(arrs)):
		heapq.heappush(h, (arrs[i][0],i))
		arrs[i] = arrs[i][1:]
	
	while len(h) > 0:
		cur = heapq.heappop(h)
		res.append(cur[0])
		idx = cur[1]
		if arrs[idx] and len(arrs[idx]) > 0:
			heapq.heappush(h, (arrs[idx][0],idx))
			arrs[idx] = arrs[idx][1:]
		elif arrs[idx] and len(arrs[idx]) == 0:
			arrs[idx] = None
			count -= 1
	return res

print kMerge(3,[[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]])
1.merge2个复杂度多少？k个多少？
knlog(n)
2.比较优缺点 为什么 kway merge 比 2way merge 好
merge2: 浪费临时存储空间
每次中间的临时都要存储到disk里面去，然后还要读出来，就慢很多
kmerge:节省空间
	
3.k个array 在k个文件里，每个文件4G，memery2个G（外部排序）
kmerge,每次merge 2G
每个文件读2G/K，好要留点给排好序的部分

		
	
	
	
	
	
	