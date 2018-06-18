"""
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
always insert at the leave
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
        cur = root
        while cur != node:
            if cur.val < node.val:
                if cur.right == None:
                    cur.right = node
                cur = cur.right
            elif cur.val >=  node.val:
                if cur.left == None:
                    cur.left = node
                cur = cur.left
        return root
                    