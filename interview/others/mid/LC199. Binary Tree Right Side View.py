"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#bfs
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, level = [], deque()
        if root != None:
            level.append(root)
        while len(level) > 0:
            res.append(level[-1].val)
            size = len(level)
            for _ in range(size):
                node = level.popleft()
                if node.left != None:
                    level.append(node.left)
                if node.right != None:
                    level.append(node.right)
        return res

#topDown dfs
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path, stk = [], []
        if root != None:
            stk.append((root, 0))
        while len(stk) > 0:
            node, height = stk.pop()
            if len(path) <= height:
                path.append(node.val)
            else:
                path[height] = node.val
            if node.right != None:
                stk.append((node.right, height + 1))
            if node.left != None:
                stk.append((node.left, height + 1))
        return path     
        
#bottomUp, from null
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        left, right = self.rightSideView(root.left), self.rightSideView(root.right)
        for i in range(len(right), len(left)):
            right.append(left[i])
        return [root.val] + right           