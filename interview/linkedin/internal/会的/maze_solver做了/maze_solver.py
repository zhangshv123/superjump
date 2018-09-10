def hasWay(matrix, start, end):
	visited = set()
	visited.add(start)
	path = []
	path.append([start[0],start[1]])
	res = []
	dfs(start, end, visited, path, res, matrix)
	return res
	
		

def dfs(cur, end, visited, path, res, matrix):
	if cur == end:
		res.append(path[:])
		return
	directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
	for dire in directions:
		new_x = cur[0] + dire[0]
		new_y = cur[1] + dire[1]
	
		if new_x < 0 or new_y < 0 or new_x > len(matrix)-1 or new_y > len(matrix[0])-1: 
			continue
		if (new_x, new_y) in visited:
			continue
		if matrix[new_x][new_y] == "B":
			continue
		
		path.append([new_x,new_y])
		visited.add((new_x, new_y))
		dfs((new_x, new_y), end, visited, path, res, matrix)
		visited.remove((new_x, new_y))
		path.pop()

matrix = [["#","#","B","B"],["#","#","#","#"],["B","B","#","#"],["#","#","#","#"]]
print hasWay(matrix, (0,0), (3,3))
		
	