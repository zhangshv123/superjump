"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].

先检查最大深度，再根据节点所处的深度放进结果。
"""

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        height_map = defaultdict(list)
        if root != None:
            self.getHeight(root, height_map)
        return map(lambda tuple:tuple[1], sorted(height_map.items()))
        # sorted(height_map.items())  跟上面一行等价
        # res = []
        # for c in height_map:
        #     res.append(height_map[c])
        # return res
        
    def getHeight(self, root, height_map):
        """
        :root is ganrantted not to be None
        :type root: TreeNode
        :rtype: int
        """
        #base
        if root == None:
            return 0 
        #recursive
        leftHeight = self.getHeight(root.left, height_map)
        rightHeight = self.getHeight(root.right, height_map)
        height = max(leftHeight, rightHeight) + 1
        height_map[height].append(root.val)
        return height
        