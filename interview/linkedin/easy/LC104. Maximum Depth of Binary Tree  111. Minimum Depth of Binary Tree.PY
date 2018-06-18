"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left,right) + 1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left != None and root.right == None:
            return leftDepth + 1
        elif root.left == None and root.right != None:
            return rightDepth + 1
        else:
            return min(leftDepth, rightDepth) + 1            