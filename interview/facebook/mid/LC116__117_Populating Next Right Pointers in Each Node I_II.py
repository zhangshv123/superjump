#!/usr/bin/python
"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
"""
题解：
这道题解法还是挺直白的，如果当前节点有左孩子，那么左孩子的next就指向右孩子。如果当前节点有右孩子，那么判断，如果当前节点的next是null，
说明当前节点已经到了最右边，那么右孩子也是最右边的，所以右孩子指向null。如果当前节点的next不是null，那么当前节点的右孩子的next就需要
指向当前节点next的左孩子。
递归求解就好。
"""
class Solution:
  # @param root, a tree link node
  # @return nothing
    def connect(self, root):
        if root == None:
            return 
        if root.left != None:
            root.left.next = root.right
            if root.next != None:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)


"""
II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
            1
         /  \
        2    3
      / \    \
     4   5    7
After calling your function, the tree should look like:
            1 -> NULL
         /  \
        2 -> 3 -> NULL
      / \    \
     4-> 5 -> 7 -> NULL
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#bottomUp 返回rightSideView, leftSideView, 连起来
class Solution:
    # @param root, a tree link node
    # @return nothing
    def helper(self, root):
        if root is None:
            return ([], [])
        leftleftSideView, leftrightSideView = self.helper(root.left)
        righleftSideView, rightrightSideView = self.helper(root.right)
        #connect
        for i in range(min(len(leftrightSideView), len(righleftSideView))):
            leftrightSideView[i].next = righleftSideView[i]
        #get root's return
        rootLeftSideView, rootRightSideView = leftleftSideView, rightrightSideView
        for i in range(len(rootLeftSideView), len(righleftSideView)):
            rootLeftSideView.append(righleftSideView[i])
        for i in range(len(rootRightSideView), len(leftrightSideView)):
            rootRightSideView.append(leftrightSideView[i])           
        return ([root] + rootLeftSideView, [root] + rootRightSideView)
    def connect(self, root):
        self.helper(root)

#dfs topDown扫遍
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        path, stk = [], []
        if root != None:
            stk.append((root, 0))
        while len(stk) > 0:
            node, height = stk.pop()
            if len(path) <= height:
                path.append(node)
            else:
                path[height].next = node
                path[height] = path[height].next
            if node.right != None:
                stk.append((node.right, height + 1))
            if node.left != None:
                stk.append((node.left, height + 1)) 
"""
bfs扫层
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level = []
        if root != None:
            level.append(root)
        while len(level) > 0:
            new_level = []
            for i, node in enumerate(level):
                if node.left != None:
                    new_level.append(node.left)
                if node.right != None:
                    new_level.append(node.right)
                if i < len(level) - 1:
                    node.next = level[i + 1]
            level = new_level
            
"""
递推：在第i层的所有next pointer都连接好的情况下，如何连接第i+1层的next pointer?
显然从第i层的最左节点开始依次通过next pointer遍历这一层，同时将他们的children，即第i+1层的节点依次通过next pointer连接起来。连接的时候要分情况处理。
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root != None:
            tempChild = TreeLinkNode(0)
            currentChild = tempChild
            while root != None:
                if root.left != None:
                    currentChild.next = root.left
                    currentChild = currentChild.next
                if root.right != None:
                    currentChild.next = root.right
                    currentChild = currentChild.next
                root = root.next
            root = tempChild.next
           