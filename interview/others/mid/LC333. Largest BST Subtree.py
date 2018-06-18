"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def helper(self, root):
        if root is None:
            return (0, True, None, None)
        leftNum, isLeftBST, leftMin, leftMax = self.helper(root.left)
        rightNum, isRightBST, rightMin, rightMax = self.helper(root.right)
        #check root is BST
        isRootBST = isLeftBST and isRightBST and (root.left == None or root.val > leftMax) and (root.right == None or root.val < rightMin)
        rootNum = leftNum + rightNum + 1 if isRootBST else max(leftNum, rightNum)
        rootMin = leftMin if root.left != None else root.val
        rootMax = rightMax if root.right != None else root.val
        return (rootNum, isRootBST, rootMin, rootMax)
        
    
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]