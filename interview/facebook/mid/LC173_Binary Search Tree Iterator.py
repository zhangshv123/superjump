"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    stk = []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        while root != None:
            self.stk.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk) > 0

    def next(self):
        """
        :rtype: int
        """
        res = self.stk.pop()
        if res.right != None:
            node = res.right
            while node != None:
                self.stk.append(node)
                node = node.left
        return res.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# 变种：pre-order
"""
example tree:
     1
   / | \
  2  3  4
/|\    |
5 8 6   7
   / \
  9   10

上来贴了一个树和一个node结构，说要完成这么个function。我没懂什么顺序，prev_node到底指啥，就问了一下，最后讨论出来可以按照pre-order顺序看，
 Order: 1, 2, 5, 8, 6, 9, 10, 3, 4, 7-google 
在这里，input不是root，而是target，可以是tree里任何一个node,找它的prev_node。
input：2  output: 1
input: 3  output: 10
input: 4  output: 3
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.children = []

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = [root]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stk.pop()
        for child in node.children[::-1]:
            self.stk.append(child)
        return node.val
        












