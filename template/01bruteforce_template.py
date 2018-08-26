代表有n个苹果，每次可以最多拿n个，返回所有的可能性
比如：n = 2
返回 [[0, 0], [0, 1], [1, 0], [1, 1]]
def printN(n):
	res = []
	dfs(n,0,res, [],[0,1])
	return res

def dfs(n, idx, res, path, possible):
	if idx == n:
		res.append(path[:])
		return
	
	for pos in possible:
		path.append(pos)
		dfs(n, idx+1, res, path, possible)
		path.pop()
		
这道题其实idx没有直接用到，所以第10行可以变成“if len(path) == n:“
idx保留在这里因为万一其他题目用得上

print printN(2)
	