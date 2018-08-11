题目：
https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pearson/04GreedyAlgorithms-2x2.pdf
有一堆job : arr = [(s1,e1), (s2, e2), (s3, e3)] 
找到arrs里面不重叠的最多的subset
贪心算法：永远找结束最早的放进去
def intervalScheduling(arrs):
	arrs.sort(key = lambda x:x[1])
	res =[arrs[0]]
	i = 1
	while i < len(arrs):
		if arrs[i][0] < res[-1][1]:
			i += 1
		else:
			res.append(arrs[i])
	return len(res)

print intervalScheduling([(0,6),(1,4),(3,5),(3,8),(4,7),(5,9),(6,10),(8,11)])
	
	