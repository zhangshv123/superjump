from collections import OrderedDict
class Solution(object):
	def findItinerary(self, tickets):
		s = []
		for ticket in tickets:
			s.append(ticket[0])
			s.append(ticket[1])
		cities = list(set(s)) #挑出所有的城市名称，并且按照字母排序
		
		dnum = [0]*len(cities)  # idx: 城市名 的map
		n = len(cities) # n表示城市的数量
		dvar = {} #城市名: idx 的map
		idx = 0
		start_city = 0
		for k in cities:
			dnum[idx] = k
			dvar[k] = idx
			if k == 'JFK': #因为从JFK开始
				start_city = idx
			idx += 1

		left = 0 # 还剩下多少张机票
		edges = [[0 for i in range(n)] for j in range(n)] #构造邻接矩阵
		for ticket in tickets:
			edges[dvar[ticket[0]]][dvar[ticket[1]]] += 1
			left += 1
		
		res = ["JFK"]
		if self.dfs(dnum, edges, start_city, left, res):
			return res
		else: #有可能一次旅行不能用完所有的机票
			return None
					
	def dfs(self, dnum, edges, cur_city, left, res):
		if left == 0:
			return True
		for j in range(len(dnum)):
			if edges[cur_city][j] > 0:
				res.append(dnum[j])
				edges[cur_city][j] -= 1
				if self.dfs(dnum, edges, j, left-1, res):
					return True
				edges[cur_city][j] += 1
				res.pop()
		return False
		
s = Solution()
print s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print s.findItinerary([["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]])
