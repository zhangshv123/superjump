"""
To find the maximum ,we can enumerate how digits we should get from nums1 , we suppose it is i.

So , the digits from nums2 is K - i.

And we can use a stack to get the get maximum number(x digits) from one array.

OK, Once we choose two maximum subarray , we should combine it to the answer.

It is just like merger sort.

In other words,we should judge which subarry is bigger than the other.


"""
def maxNumber(self, nums1, nums2, k):

	def prep(nums, k):
		drop = len(nums) - k
		out = []
		for num in nums:
			while drop and out and out[-1] < num:
				out.pop()
				drop -= 1
			out.append(num)
		return out[:k]

	def merge(a, b):
		return [max(a, b).pop(0) for _ in a+b]

	return max(merge(prep(nums1, i), prep(nums2, k-i))
			   for i in range(k+1)
			   if i <= len(nums1) and k-i <= len(nums2))