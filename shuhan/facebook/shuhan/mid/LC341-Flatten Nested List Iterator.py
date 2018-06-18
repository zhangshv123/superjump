#!/usr/bin/python
class NestedIterator(object):
	def flatten_nestedList(self, nestedInteger):
		if nestedInteger.isInteger():
			return [nestedInteger]
		else:
			flatten_list = []
			for sub_nestedInteger in nestedInteger.getList():
				flatten_list += self.flatten_nestedList(sub_nestedInteger)
			return flatten_list
	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.flatten_list = []
		self.index = -1
		for nestedInteger in nestedList:
			self.flatten_list += self.flatten_nestedList(nestedInteger)
		
	def next(self):
		"""
		:rtype: int
		"""
		self.index += 1
		return self.flatten_list[self.index]

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.index + 1 < len(self.flatten_list)
		