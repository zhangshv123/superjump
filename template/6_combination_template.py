#combination
#input: n, m
#n is an array of [1, 2, ..., n]
#choose m from n, order do not matter

def combination(n, m):
	res = []
	dfs(n, m, res, [], 0)
	return res
	
def dfs(n, m, res, path, index):
	# clear your definition
	# n = 10, m = 5, res = [...], path = [0, 3, 5], index = 8
#	step 1: pick new i from(index,n)选一个新的螺丝
#	step 2: path.append(i)换上新的螺丝
#	step 3: dfs(n, m, res, path, i+1)交给小弟
#	step 4: path.pop()换掉螺丝，方便交给上级
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


