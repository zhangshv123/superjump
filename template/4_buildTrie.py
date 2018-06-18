class TrieNode(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.isWord = False
class Solution(object): 
	def buildTrie(self, words):
		"""
		:type board: List[str]
		:rtype:TrieNode
		"""
		root = TrieNode()
		for word in words:
			node = root
			for c in word:
				if c not in node.children:
					node.children[c] = TrieNode()
				node = node.children[c]
			node.isWord = True
		return root