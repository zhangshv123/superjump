"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#dfs版本
class Codec:

    def serialize(self, root):
        res = []
        self.dfs(root, res)
        return "[" + ",".join(res) + "]"
        
    def dfs(self, node, res):
        if not node:
            res.append("null")
            return
        
        res.append(str(node.val))
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        

    def deserialize(self, data):
        nodes = data[1:-1].split(",")
        idx = [0]
        return self.helper(nodes, idx)
        
        
    def helper(self, nodes, idx):
        if nodes[idx[0]] == "null":
            idx[0] += 1
            return None
        root = TreeNode(int(nodes[idx[0]]))
        idx[0] += 1
        root.left = self.helper(nodes, idx)
        root.right = self.helper(nodes, idx)
        
        return root

#bfs版本
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        res = []
        while len(q) > 0:
            cur = q.popleft()
            if cur:
                res.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print data
        nodes = []
        for item in data[1:-1].split(","):
            if item != "null":
                nodes.append(TreeNode(int(item)))
            else:
                nodes.append(None)
        q = deque()
        q.append(nodes[0])
        index = 0
        while len(q) > 0:
            cur = q.popleft()
            if cur:
                cur.left = nodes[index + 1]
                cur.right = nodes[index + 2]
                q.append(cur.left)
                q.append(cur.right)
                index += 2
        return nodes[0]

见
https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/                
follow up:
1. 如果 tree 是 bst？(preorder 或者 postorder)
那我们可以存 either  preorder or postorder traversal

2. 如果 tree 是 complete tree：(bst做)
complete tree是除 all levels are completely filled except possibly the last level and
all nodes of last level are as left as possible(heap)
level order tranversal is sufficient to store the tree
we know the firt node is the root, next two nodes are nodes of next level. next four
nodes are nodes of 2nd level and so on.

3. 如果是 full tree:（preorder）
full tree is a binary tree where every node has either 0 or 2 children. 
simply store preorder tranversal and store a bit with every node to indicate whether the node
is an internal node or a leaf node.

4.general binary tree
a simple solution is store both inorder and preorder traversals.
this solution requires space twice the size of Binary tree. We can save space 
by storing preorder traversal and a marker for NULL pointers.


