# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        p = root.left
        
        if not p:
            return 
        
        while p.right:
            p = p.right
        
        p.right = root.right
        root.right = root.left
        root.left = None
"""
和LC原题不同的是，返回的是Doubled Linked List，并且顺序是树的Inordered Traversal。
”“”