"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
"""
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None
            idx = left
            for i in range(left, right + 1):
                if nums[i] > nums[idx]:
                    idx = i
            root = TreeNode(nums[idx])
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)
            return root
        return helper(0, len(nums) - 1)


class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		if not nums:
			return None
		return self.helper(nums,0,len(nums)-1)
	
	def helper(self,nums,start,end):
		if start >end:
			return None
		
		idxMax = start
		for i in range(start+1,end+1):
			if nums[idxMax] < nums[i]:
				idxMax = i
		
		root = TreeNode(nums[idxMax])
		
		root.left = self.helper(nums, start, i-1)
		root.right = self.helper(nums, i+1, end)
		
		return root
