import heapq
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
		
	
	
	
	
	
	