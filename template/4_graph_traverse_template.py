给一个连接矩阵，输出矩阵对应的图的每个cluster。
比如说：
	A B C D E
A [0 1 0 0 0]
B [1 0 1 0 0]
C [0 1 0 0 0]
D [0 0 0 0 1]
E [0 0 0 1 0]

所以图有如下的边:
A - B
B - C
D - E
所以输出是: [(A,B,C), (D,E)]
def findCluster(matrix):
	n = len(matrix) # number of nodes
	res = [] # output, list of connected components
	visited = set() # nodes in found connected components
	
	for i in range(n): # find the next connected component from i
		if i in visited: #因为visited是全局标黑，所以没有pop
			continue
		cp = [i]
		visited.add(i)
		dfs(matrix, i, visited, cp)
		res.append(cp)
	return res
	

def dfs(matrix, cur, visited, cp): # traversal
	for i in range(len(matrix)):
		if matrix[cur][i] == 1 and i not in visited:
			cp.append(i)
			visited.add(i)
			dfs(matrix, i, visited, cp)
			
			
print findCluster([[0,1,0,0,0],[1,0,1,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]])
			
