#这道题让我们在常数时间范围内实现插入删除和获得随机数操作，如果这道题没有常数时间的限制，那么将会是一道非常简单的题，我们直接用一个set就可以搞定所有的操作。但是由于时间的限制，我们无法在常数时间内实现获取随机数，所以只能另辟蹊径。此题的正确解法是利用到了一个一维数组和一个哈希表，其中数组用来保存数字，哈希表用来建立每个数字和其在数组中的位置之间的映射，对于插入操作，我们先看这个数字是否已经在哈希表中存在，如果存在的话直接返回false，不存在的话，我们将其插入到数组的末尾，然后建立数字和其位置的映射。删除操作是比较tricky的，我们还是要先判断其是否在哈希表里，如果没有，直接返回false。由于哈希表的删除是常数时间的，而数组并不是，为了使数组删除也能常数级，我们实际上将要删除的数字和数组的最后一个数字调换个位置，然后修改对应的哈希表中的值，这样我们只需要删除数组的最后一个元素即可，保证了常数时间内的删除。而返回随机数对于数组来说就很简单了，我们只要随机生成一个位置，返回该位置上的数字即可，参见代码如下：
#http://www.cnblogs.com/grandyang/p/5740864.html
import random
class RandomizedSet(object):

	def __init__(self):
		self.List = []
		self.Map = dict()

	def insert(self, val):
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		if val not in self.Map:
			self.Map[val] = len(self.List)
			self.List.append(val)
			return True
		return False

	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		if val not in self.Map:
			return False
			
		idx, last = self.Map[val], self.List[-1]
		self.List[idx], self.Map[last] = last, idx
		self.List.pop()
		del self.Map[val] # delete map entry in python
		return True

	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		index = random.randint(0, len(self.List) - 1)
		return self.List[index]
		
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
