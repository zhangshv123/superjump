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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        if root is None:
            return []
        res = []
        res += self.searchRange(root.left, k1, k2)
        if root.val >= k1 and root.val <= k2:
            res.append(root.val)
        res += self.searchRange(root.right, k1, k2)
        return res 