一个图是一个tree需要满足2点
1.全联通图：e = v - 1
2.无环
这道题用bfs就可以，首先需要建临接表
建图很简单，map的key对应每个 vertice， value对应每个vertice的neighbors,用arraylist表示。 遍历edges,每个edge[] 分别代表一条edge的两端，分别加到彼此的邻居里。这里有一个E = V - 1要注意，如果不满足就直接返回false. 用Queue做bfs, 用一个boolean[]  visited记录是否访问过，先把0放进去。每次从queue里取出一个，如果这个已经被访问过，立马返回false.  为什么？这种情况只可能出现在环里，你在queue里放进去过这个元素好几次。 然后访问poll出来这个点的邻接表，把没有访问过的元素offer到队列。最后我们要保证每个元素都被访问过，如果有没访问过的就返回false.

链接：https://www.jianshu.com/p/54d719cae3f4

#一般能用dfs就用dfs不容易写错：
from collections import defaultdict
class Solution(object):
	def validTree(self, n, edges):
		graph = defaultdict(list)
		visited = set()
		visited.add(0)
		self.buildGraph(graph, edges)
		return self.dfs(0, None, graph, visited) and len(visited) == n
		
	def buildGraph(self, graph, edges): #建立邻接表
		for edge in edges:
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])
		return
	
	def dfs(self, node, parent, graph, visited): 	
		for child in graph[node]:
			if child not in visited:
				visited.add(child)
				if not self.dfs(child, node, graph, visited): #只要有loop发生就直接返回false
					return False
			else:
				if child != parent: #因为是无向图，所以可能是来自于parent
					return False
		return True


from collections import defaultdict, deque
class Solution(object):
	def validTree(self, n, edges):
		if n != len(edges) + 1:
			return False
		visited = set()
		edges.sort()
		d = defaultdict(list)
		self.buildGraph(d, edges)
		q = deque()
		q.append(0)
		while len(q) > 0:
			cur = q.popleft()
			if cur in visited:
				return False
			visited.add(cur)
			for nei in d[cur]:
				if nei not in visited:
					q.append(nei)
		return True if len(visited) == n else False
		
	
	def buildGraph(self, graph, edges):
		for edge in edges:
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])
		return
			
		

s = Solution()
print s.validTree(5, [[0,1],[0,4],[1,4],[2,3]])
print s.validTree(5, [[0,1], [0,2], [0,3], [1,4]])