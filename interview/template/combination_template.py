#combination
#input: n, m
#n is an array of [1, 2, ..., n]
#choose m from n

def combination(n, m):
	res = []
	dfs(n, m, res, [], 0)
	return res
	
def dfs(n, m, res, path, index):
	# clear your definition
	# n = 10, m = 5, res = [...], path = [0, 3, 5], index = 8
#	step 1: pick new i from(index,n)
#	step 2: path.append(i)
#	step 3: dfs(n, m, res, path, i+1)
#	step 4: path.pop()
#	repeat 1-4 until done:因为需要所有螺丝的可能性
	if len(path) == m:
		res.append(path[:])
		return
	
	for i in range(index,n):
		if i in path:
			continue
		path.append(i)
		dfs(n, m, res, path, i+1)
		path.pop()
	
print combination(3, 2)


