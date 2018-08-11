题目：
给出一个arr, 如[0,1,0,1,0]，每个1就是一个发电厂，然后给出一个range，比如是2，就是说每个发电厂能cover前后range为2的距离，然后求需要的发电厂的最少数。e.g.[1,1,0], range 为 1 -> [0,1,0]
思路：
1.确定这是一个greedy的问题，所以local 最优 = global 最优
2.准备一个opt数组存结果，greedy和dfs不一样是因为greedy不会回头，dfs是穷举，可能会反悔！greedy不会反悔！
sudo code:
	look for land:
		if land is covered by opt:
			continue
	else:
		find rightest最右边的 power plant that covers this land.
		append the new power plant index into opt  
def putPower(arr, r):
	opt = []
	for i in range(len(arr)):
		if arr[i] == 0: #如果是土地
			if len(opt) == 0:
				if i+r < len(arr):
					if arr[i+r] == 1:
						opt.append(i + r)
					else:
						return []
				elif i - r < len(arr):
					if arr[i-r] == 1:
						opt.append(i - r)
					else:
						return []
			else:
				if i > opt[-1] + r: #当前的土地不能被已有的电厂cover，需要找一个新的电厂
					changed = False
					start = min(len(arr)-1, i+r)#为防止越界
					end = max(-1,i-r-1)#同上
					for j in range(start, end, -1):
						if arr[j] == 1:
							opt.append(j)
							changed = True
					if not changed:
						return []
	return opt
						 


print putPower([0,1,0,1,0], 1)
print putPower([1,1,0], 1)
print putPower([1,1,1], 1)
print putPower([0,0,1], 1)
		