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
            for j in range(i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
#niuniu version

        for i in range(1,n+1):
             #以j为root
            for j in range(1,i+1):
                #dp[i]:有i个数的子问题
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n] on
"""
II your program should return all 5 unique BST's shown below.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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