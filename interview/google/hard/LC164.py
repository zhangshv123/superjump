"""
bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
"""

"""
maximumGap
Suppose there are N elements in the array, the min value is min and the max value is max. Then the maximum gap will be no smaller than ceiling[(max - min ) / (N - 1)].

Let gap = ceiling[(max - min ) / (N - 1)]. We divide all numbers in the array into n-1 buckets, where k-th bucket contains all numbers in [min + (k-1)gap, min + k*gap). Since there are n-2 numbers that are not equal min or max and there are n-1 buckets, at least one of the buckets are empty. We only need to store the largest number and the smallest number in each bucket.

After we put all the numbers into the buckets. We can scan the buckets sequentially and get the max gap.
"""
import math
class Solution:
	# @param num, a list of integer
	# @return an integer
	def maximumGap(self, nums):
		num = list(set(nums))
		if len(num) < 2 or min(num) == max(num):
			return 0
		a, c = min(num), max(num)
		size = int(math.ceil((c-a)/(len(num)-1)))
		bucket = [[None, None] for _ in range((c-a)/size +1)]
		for n in num:
			b = bucket[(n-a)/size]
			b[0] = n if b[0] is None else min(b[0], n)
			b[1] = n if b[1] is None else max(b[1], n)
		bucket = [b for b in bucket if b[0] is not None]
		return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))
sol = Solution()
print sol.maximumGap([1,2,4,2])