
"""
Flatten Binary Tree To Linked List变形。和LC原题不同的是，返回的是Doubled Linked List，并且顺序是树的Inordered Traversal。
https://www.youtube.com/watch?v=Dte6EF1nHNo
"""
class Node(object):
	def __init__(self):
		self.value = 0
		self.left, self.right = None, None
class Solution(object):
#	<- 1 <-> 2 <-> 3 ->   <-4 <-> 5 <-> 6 -> 
	def concatenate(a, b):
		if a == None:
			return b
		if b == None:
			return a
		aEnd, bEnd = a.left, b.left
		a.left = bEnd
		bEnd.right = a
		aEnd.right = b
		b.left = aEnd
		return a
	def treeToList(self, root):
		if n == None:
			return n
		left, right = self.treeToList(root.left), self.treeToList(root.right)
		n.left, n.right = n, n
		n = self.concatenate(left, n)
		n = self.concatenate(n, right)
		return n