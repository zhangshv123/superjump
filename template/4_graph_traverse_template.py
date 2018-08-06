给一个连接矩阵，输出矩阵对应的图的每个cluster。
比如说：
	A B C D E
A  [0 1 0 0 0]
B  [1 0 1 0 0]
C  [0 1 0 0 0]
D  [0 0 0 0 1]
E  [0 0 0 1 0]

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
		cp = [i] #相当于result
		visited.add(i)
		dfs(matrix, i, visited, cp)
		res.append(cp[:])
	return res
	

def dfs(matrix, cur, visited, cp): # traversal
	for i in range(len(matrix)):
		if matrix[cur][i] == 1 and i not in visited:
			cp.append(i)
			visited.add(i)
			dfs(matrix, i, visited, cp)
			
			
print findCluster([[0,1,0,0,0],[1,0,1,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]])
#输出[[0, 1, 2], [3, 4]]

遍历/穷举模板
def helper(m , i, path, visited, res)
m: input
i: 当前节点
path: 从起点到当前节点的路径(一般都需要pop)
visited: 哪些节点还可以访问
res:结果，变化大，看当前的题意(一般不需要pop)

遍历和穷举的区别：
1.遍历往往时间复杂度是线性的，因为每个节点只需访问一遍,顺序无所谓
2.穷举是指数级的，每个节点访问不止一遍，顺序有所谓！
	
			
