#!/usr/bin/python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
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
                
