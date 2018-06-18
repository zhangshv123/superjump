#!/usr/bin/python
def maxSubArrayLen(nums, k):
	""
	可以用hash表来保存前n个数的和,然后每次去查是否当前和与目标值之差已经存在, 是的话说明我们找到了一个序列,然后更新最大长度大小. 哦, 还有就是如果有相同的和, 那就不管了, 因为我们要的最长的子串, 肯定是留着前面的一个值更优.
	""
	d = dict()
	size, res = len(nums),0
	total = 0
	d[0] = 0
	for i in range(size):
		total += nums[i]
		if total not in d:
			d[total] = i+1
		if total-k in d:
			cur = i-d[total-k]+1
			res = max(res,cur)
	print d
	return res

print maxSubArrayLen([-2,-1,2,1],1)

