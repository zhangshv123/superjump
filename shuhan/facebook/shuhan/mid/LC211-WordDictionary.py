#!/usr/bin/python
class WordDictionary(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.word_dict = collections.defaultdict(list)

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: void
		"""
		if word:
			self.word_dict[len(word)].append(word)

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could
		contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		if not word:
			return False
		if '.' not in word:
			return word in self.word_dict[len(word)]
		for v in self.word_dict[len(word)]:
			for i, char in enumerate(word):
				if v[i] !=char and char != '.':
					break
			else:
				return True
		return False
