#一個int array裡面 找出三個數相乘最大的數是多少 有正有負但沒有零
#一開始這題就掛了 只想得出N^3 後來歐洲小哥提示說可以先sort array 再從array最前面跟最後面撈數字 depends on 有多少負數存在array裡面
class Solution(object):
#	方法1：
#	Sort the array using some efficient in-place sorting algorithm in ascending order.
#	Return the maximum of product of last three elements of the array and product of first two elements and last element.
#	O(nlogn) Time, O(1) Space
	def max3Product(self,nums):
		nums = sorted(nums)
		print nums
		res = max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
		return res
s = Solution()
print s.max3Product([1, -4, 3, -6, 7, 0])

#方法2：
#O(n) Time, O(1) Space
#
#Scan the array and compute Maximum, second maximum and third maximum element present in the array.
#Scan the array and compute Minimum and second minimum element present in the array.
#Return the maximum of product of Maximum, second maximum and third maximum and product of Minimum, second minimum and Maximum element.
#Note – Step 1 and Step 2 can be done in single traversal of the array.

