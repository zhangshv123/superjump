class Solution(object):
	#和 tranverse graph非常类似！
	def countComponents(self, n, edges):
		visited = set()
		edges.sort()
		count = 0
		for edge in edges:
			if edge[0] not in visited:
				count += 1
				visited.add(edge[0])
				visited.add(edge[1])
				self.dfs(edges, visited)
		return count + n - len(visited)
	
	def dfs(self, edges, visited):
		for edge in edges:
			if edge[0] in visited and edge[1] not in visited:
				visited.add(edge[1])
				self.dfs(edges, visited)
			elif edge[1] in visited and edge[0] not in visited:
				visited.add(edge[0])
				self.dfs(edges, visited)
		return
		
				
			
			