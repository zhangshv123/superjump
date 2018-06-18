#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) / 2
        root = TreeNode(nums[mid])
        left = self.helper(nums, left, mid - 1)
        right = self.helper(nums, mid + 1, right)
        root.left, root.right = left, right
        return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)