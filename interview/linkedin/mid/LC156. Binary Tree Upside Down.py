"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
    1
   / 
  2 -- 3
 / 
4 -- 5 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
这道题让我们把一棵二叉树上下颠倒一下，而且限制了右节点要么为空要么一定会有对应的左节点。
上下颠倒后原来二叉树的最左子节点变成了根节点，其对应的右节点变成了其左子节点，
其父节点变成了其右子节点，相当于顺时针旋转了一下。对于一般树的题都会有迭代和递归两种解法，
这道题也不例外，那么我们先来看看递归的解法。对于一个根节点来说，我们的目标是将其左子节点变为根节点，
右子节点变为左子节点，原根节点变为右子节点，那么我们首先判断这个根节点是否存在，且其有没有左子节点，
如果不满足这两个条件的话，直接返回即可，不需要翻转操作。
"""
"""
iteration
下面我们来看迭代的方法，和递归方法相反的时，这个是从上往下开始翻转，直至翻转到最左子节点
"""
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        oldLeft, oldRight = None, None
        while cur != None:
            newLeft, newRight, newCur = cur.right, cur, cur.left
            cur.left, cur.right = oldLeft, oldRight
            oldLeft, oldRight, cur = newLeft, newRight, newCur
        return oldRight

"""
recursion
那么我们不停的对左子节点调用递归函数，直到到达最左子节点开始翻转，翻转好最左子节点后，
开始回到上一个左子节点继续翻转即可，直至翻转完整棵树
"""
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left is None:
            return root
        l, r = root.left, root.right
        res = self.upsideDownBinaryTree(l)
        l.left, l.right = r, root
        root.left, root.right = None, None
        return res        