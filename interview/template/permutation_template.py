#permutation
#input: n, m
#n is an array of [1, 2, ..., n]
#choose m from n,order matter

def permutation(n, m):
	res = []
	dfs(n, m, res, [])
	return res
	
def dfs(n, m, res, path):
	# clear your definition
	# n = 10, m = 5, res = [...], path = [0, 3, 5], index = 8
#	step 1: pick new i from(0,n)
#	step 2: path.append(i)
#	step 3: dfs(n, m, res, path, i+1)
#	step 4: path.pop()
#	repeat 1-4 until done:因为需要所有螺丝的可能性
	if len(path) == m:
		res.append(path[:])
		return
	
	for i in range(n):
		if i in path:
			continue
		path.append(i)
		dfs(n, m, res, path)
		path.pop()
	
print permutation(3, 2)