#!/usr/bin/python
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

          _______3______
         /              \
     ___5__          ___1__
    /      \        /      \
    6      _2       0       8
            /  \
            7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Show Company Tags
Show Tags
Show Similar Problems

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/
"""
思想：和数学归纳法一样， 提取树里的信息，得到答案
1.从子树传递上来的信息是什么？
2.自己要做什么？
hasLeft, hasRight
y           y
y           n
n           y
n           n
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q) #找root.left里面是否存在p,q,如果存在哪一个就返回哪个
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is not None:
            return right
        if right is None and left is not None:
            return left
        if left is None and right is None: #代表p,q都不在root.left里面，也不在root.right里面，所以就直接返回null
            return None
        return root


"""
分别找到p,q对应的path,遍历两个path找到最后一个相同的元素
"""
class Solution(object):
    def getPath(self, root, p):
        stk, path = [], []
        if root != None:
            stk.append((root, 0))
        while len(stk) > 0:
            node, height = stk.pop()
            if len(path) <= height:
                path.append(node)
            else:
                path[height] = node
            if node == p:
                return path[:height + 1]
            if node.left != None:
                stk.append((node.left, height + 1))
            if node.right != None:
                stk.append((node.right, height + 1))
        return []
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1, path2 = self.getPath(root, p), self.getPath(root, q)
        if len(path1) == 0 or len(path2) == 0:
            return None
        min_length = min(len(path1), len(path2))
        for i in range(1, min_length + 1):
            if i == min_length or path1[i] != path2[i]:
                return path1[i-1]
 
#niuniu version               
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        stk,path,res = [],[],[]
        if root != None:
            stk.append((root,0))
        while len(stk) > 0:
            node,height = stk.pop()
            if len(path) <= height:
                path.append(node.val)
            else:
                path[height] = node.val
            
            # base
            if node == p:
                res.append(path[:height+1])
            elif node == q:
                res.append(path[:height+1])
            if len(res) == 2:
                break
            if node.left:
                stk.append((node.left,height+1))
            if node.right:
                stk.append((node.right,height+1))
            
        i = 1
        min_length = min(len(res[0]),len(res[1]))
        for i in range(1, min_length + 1):
            if i == min_length or res[0][i] != res[1][i]:
                return res[0][i-1]

# 如果存在parent节点
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        dict = {}
        while A is not None:
            dict[A] = True
            A = A.parent

        while B is not None:
            if B in dict:
                return B
            B = B.parent

        return root

#如果2个节点可能一个存在，一个不存在tree里面，或者2个都不存在tree里面
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        a = [False]
        res = self.dfs(root, p, q, a)
        if a[0] is True:
            return res
        else:
            return None

    def dfs(self, root, p, q, a):
        """
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.dfs(root.left, p, q, a)
        right = self.dfs(root.right, p, q, a)
        if root == p or root == q:
            if left or right:
                # found the LCA
                a[0] = True
                return root
            else:
                return root
        if left and not right:
            return left
        if right and not left:
            return right
        if not left and not right:
            return None
        # found the LCA
        a[0] = True
        return root
        
