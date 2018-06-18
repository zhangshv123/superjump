"""

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: int 多少个
        :rtype: boolean 自己是Uni?
        """
        if root is None:
            return (0, True)
        leftNum, isLeftUni = self.helper(root.left)
        rightNum, isRightUni = self.helper(root.right)
        isRootUni = isLeftUni and isRightUni and (root.left == None or root.val == root.left.val) and (root.right == None or root.val == root.right.val)
        rootNum = leftNum + rightNum + 1 if isRootUni else leftNum + rightNum
        return (rootNum, isRootUni)
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]



        