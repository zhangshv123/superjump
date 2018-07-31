from random import *
class RandomizedSet(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.map = dict()
		self.dataList = []
		

	def insert(self, val):
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		if val not in self.map:
			self.dataList.append(val)
			self.map[val] = len(self.dataList)-1
			return True
		return False
		
		
	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		if val in self.map:
			idx = self.map[val]
			self.map[self.dataList[-1]] = self.map[val]
			del self.map[val]
			self.dataList[idx], self.dataList[-1] = self.dataList[-1], self.dataList[idx]
			self.dataList.pop()
			return True
		return False
		

	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		idx = randint(0, len(self.dataList)-1)
		print self.map,self.dataList
		return self.dataList[idx]

# Init an empty set.
randomSet = RandomizedSet();

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
print randomSet.insert(1);

# Returns false as 2 does not exist in the set.
print randomSet.remove(2);

# Inserts 2 to the set, returns true. Set now contains [1,2].
print randomSet.insert(2);

# getRandom should return either 1 or 2 randomly.
print randomSet.getRandom();

# Removes 1 from the set, returns true. Set now contains [2].
print randomSet.remove(1);

# 2 was already in the set, so return false.
print randomSet.insert(2);

# Since 2 is the only number in the set, getRandom always return 2.
#print randomSet.getRandom();