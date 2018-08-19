#!/usr/bin/python
"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
用到二叉搜索树的性质. 因此我们还可以比较给定结点与根结点的大小, 如果根节点的值较大, 说明这个结点在根节点的左边, 
因此此时根节点就是其不紧切后继, 然后再往左子树去比较. 如果根节点值较小, 说明我们要找的结点在根节点右边.
这样一步步就可以找到最终的后继.
"""
"""
给出一个平衡二叉树, 一个 target value 找到 the previous element.
用两种方法解.
"""
# Top Solution
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rty
        """
        if root is None:
            return None
        print root.val
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left != None else root
iterative Solution
思路：
1.有右儿子，就找右儿子里面值最小的
2.没有右儿子，就search找到最后一个比自己大的值
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def inorderSuccessor(self, root, p):
        res = None
        if p.right:
            return self.minValue(p.right)
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return res
    
    def minValue(self, p):
        left, right = p.val, p.val
        if p.left:
            left = self.minValue(p.left)
        elif p.right:
            right = self.minValue(p.right)
        return min(left,right,p)

    
