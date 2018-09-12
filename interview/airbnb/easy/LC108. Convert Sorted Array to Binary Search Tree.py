#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
时间复杂度还是一次树遍历O(n)
总的空间复杂度是栈空间O(logn)加上结果的空间O(n)，额外空间是O(logn)，总体是O(n)
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums or len(nums) == 0:
            return None
        return self.convert(nums, 0, len(nums)-1)

    def convert(self,nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        mid = (start + end)/2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, start, mid-1)
        root.right = self.convert(nums, mid+1, end)
        return root