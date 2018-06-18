#!/usr/bin/python
class BSTIterator:
#	这个题目不错！要多看！
#	复杂度：O(h) memory, hasNext() in O(1) time,
#	But next() is O(h) time.
	def __init__(self, root):
		self.stack = []
		self.pushAll(root)

	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		return self.stack

	# @return an integer, the next smallest number
	def next(self):
		tmpNode = self.stack.pop()
		self.pushAll(tmpNode.right)
		return tmp ode.val
		
	def pushAll(self, node):
		while node is not None:
			self.stack.append(node)
			node = node.left
