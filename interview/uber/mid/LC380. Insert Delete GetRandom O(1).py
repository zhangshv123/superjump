insert(val): 将val添至dataList末尾，并在dataMap中保存val的下标idx

remove(val): 记val的下标为idx，dataList末尾元素为tail，弹出tail并将其替换至idx处，在dataMap中更新tail的下标为idx，最后从dataMap中移除val

getRandom: 从dataList中随机选取元素返回
from random import *
class RandomizedSet(object):

	def __init__(self):
		self.map = dict()
		self.dataList = []
		

	def insert(self, val):
		if val not in self.map:
			self.dataList.append(val)
			idx = len(self.dataList) - 1
			self.map[val] = idx
			return True
		return False
		
	def remove(self, val):
		if val in self.map:
			idx, last = self.map[val], self.dataList[-1]
			self.dataList[idx], self.map[last] = last, idx
			self.dataList.pop()
			del self.map[val]
			return True
		return False

	def getRandom(self):
		idx = randint(0, len(self.dataList)-1)
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