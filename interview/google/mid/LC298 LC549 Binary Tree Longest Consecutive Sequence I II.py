"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        def dfs(root, count, target):
            if root == None:
                return 0
            if root.val == target:
                count += 1
            else:
                count = 1
            return max(count, dfs(root.left, count, root.val + 1), dfs(root.right, count, root.val + 1))
        return dfs(root, 0, root.val)

"""
II Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered 
valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where 
not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
""" 
"""
定义函数solve(root)，递归求解以root为根节点向子节点方向（parent-child）的路径中，最大连续递增路径长度inc，以及最大连续递减路径长度dec

则以root为根节点的子树中，最大连续路径长度=inc + dec + 1（路径不包含root）
"""
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def dfs(root):
            if root == None:
                return (0, 0)
            irt, drt = 0, 0
            for c in (root.left, root.right):
                if c == None:
                    continue
                ic, dc = dfs(c)
                if root.val == c.val - 1:
                    irt = max(irt, ic)
                if root.val == c.val + 1:
                    drt = max(drt, dc)
            nonlocal res
            res = max(res, irt + drt + 1)
            return (irt + 1, drt + 1)
        dfs(root)
        return res               
        