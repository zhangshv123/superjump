#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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