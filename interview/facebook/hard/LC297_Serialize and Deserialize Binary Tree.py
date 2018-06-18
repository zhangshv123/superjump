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
                    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))