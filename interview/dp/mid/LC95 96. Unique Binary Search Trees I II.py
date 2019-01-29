"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, 

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
I return number of diff trees   
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        #dp[i]:有i个数的子问题
        for i in range(1, n + 1):
            #以j为root
            for j in range(1,i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
"""
II your program should return all 5 unique BST's shown below.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
请参考：
https://blog.csdn.net/fuxuemingzhu/article/details/80778651

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.generateBST(1, n)
        
    def generateBST(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start,end+1):
            left_nodes = self.generateBST(start, i-1)
            right_nodes = self.generateBST(i+1, end)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res




class Solution(object):
    def cloneTree(self, node, offSet):
        if node == None:
            return None
        newNode = TreeNode(node.val + offSet)
        newNode.left = self.cloneTree(node.left, offSet)
        newNode.right = self.cloneTree(node.right, offSet)
        return newNode
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                for leftNode in dp[j - 1]:
                    for rightNode in dp[i - j]:
                        root = TreeNode(j)
                        root.left = leftNode
                        root.right = self.cloneTree(rightNode, j)
                        dp[i].append(root)
        return dp[n]