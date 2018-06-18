#!/usr/bin/python
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#topDown dfs
class Solution:
    def isValidBST(self, root):
        if root is None:
            return True
        return self.isInValidRange(root, -sys.maxint, sys.maxint)
        
    def isInValidRange(self, root, min_value, max_value):
        if root is None:
            return True
        valid = root.val > min_value and root.val < max_value 
        valid &= self.isInValidRange(root.left, min_value, root.val)
        valid &= self.isInValidRange(root.right, root.val, max_value)
        return valid

#topDown dfs by stack
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stk = []
        if root != None:
            stk.append((root, -sys.maxint, sys.maxint))
        while len(stk) > 0:
            node, minVal, maxVal = stk.pop()
            if node.val <= minVal or node.val >= maxVal:
                return False
            if node.right != None:
                stk.append((node.right, node.val, maxVal))
            if node.left != None:
                stk.append((node.left, minVal, node.val))
        return True
"""
bottomUp
"""
class Solution(object):
    def helper(self, root):
        if root == None:
            return (True, None, None)
        isLeftBST, leftMin, leftMax = self.helper(root.left)
        isRightBST, rightMin, rightMax = self.helper(root.right)
        isRootBST = isLeftBST and isRightBST and (root.left == None or root.val > leftMax) and (root.right == None or root.val < rightMin)
        rootMin = leftMin if root.left != None else root.val
        rootMax = rightMax if root.right != None else root.val
        return (isRootBST, rootMin, rootMax)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]
 