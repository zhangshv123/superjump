"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
最好读懂的版本
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, node, target, path, res):
        if not node.left and not node.right and target == node.val:
            path.append(node.val)
            res.append(path[:])
            path.pop()
            return
            
        if node.left:
            path.append(node.val)
            self.dfs(node.left, target - node.val, path, res)
            path.pop()
            
        if node.right:
            path.append(node.val)
            self.dfs(node.right, target - node.val, path, res)
            path.pop()  


class Solution(object):
    def dfs(self, root, target, path, res):
        #base
        if root.left is None and root.right is None and root.val == target:
                res.append(path + [target])
        #recursion
        path.append(root.val)
        if root.left:
            self.dfs(root.left, target - root.val, path, res)
        if root.right:
            self.dfs(root.right, target - root.val, path, res)
        path.pop()
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root != None:
            self.dfs(root, sum, [], res)
        return res

# dfs 用stack实现
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stk, path, res = [], [], []
        if root != None:
            stk.append((root, sum, 0))
        while len(stk) > 0:
            node, sum, height = stk.pop()
            #add to path
            if len(path) <= height:
                path.append(node.val)
            else:
                path[height] = node.val
            #base
            if node.left == None and node.right == None and node.val == sum:
                res.append(path[:height + 1])
            #add children list
            if node.right != None:
                stk.append((node.right, sum - node.val, height + 1))
            if node.left != None:
                stk.append((node.left, sum - node.val, height + 1))
        return res
