用一个heap，每次返回price最小的那个进行拓展
heap里面存的是 （price, 地点，depth）
所以我们先存(0,src,0)
import heapq
import sys
class Solution(object):
	def findCheapestPrice(self, n, flights, src, dst, k):
		h = []
		h.append((0,src,0))
		res = sys.maxint
		changed = False
		
		while len(h) > 0:
			cur = heapq.heappop(h)
			for flight in flights:
				if flight[0] == cur[1]:
					if flight[1] == dst:
						price = cur[0]+flight[2]
						res = min(res, price)
						changed = True
					else:
						if cur[2] + 1 <= k:
							item = (cur[0]+flight[2], flight[1], cur[2]+1)
							heapq.heappush(h, item)
		return res if changed else -1

s = Solution()
print s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
print s.findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1)
print s.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
			
			
					
		