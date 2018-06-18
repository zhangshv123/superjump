#!/usr/bin/python
"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
"""
这道题让我们在常数时间范围内实现插入删除和获得随机数操作，如果这道题没有常数时间的限制，那么将会是一道非常简单的题，我们直接用一个set就可以搞定所有的操作。
但是由于时间的限制，我们无法在常数时间内实现获取随机数，所以只能另辟蹊径。此题的正确解法是利用到了一个一维数组和一个哈希表，其中数组用来保存数字，哈希表用
来建立每个数字和其在数组中的位置之间的映射，对于插入操作，我们先看这个数字是否已经在哈希表中存在，如果存在的话直接返回false，不存在的话，我们将其插入到数组
的末尾，然后建立数字和其位置的映射。删除操作是比较tricky的，我们还是要先判断其是否在哈希表里，如果没有，直接返回false。由于哈希表的删除是常数时间的，而数组
并不是，为了使数组删除也能常数级，我们实际上将要删除的数字和数组的最后一个数字调换个位置，然后修改对应的哈希表中的值，这样我们只需要删除数组的最后一个元素即可，
保证了常数时间内的删除。而返回随机数对于数组来说就很简单了，我们只要随机生成一个位置，返回该位置上的数字
"""
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.array = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        idx = self.map[val]
        self.map[self.array[-1]] = idx
        self.array[idx]= self.array[-1]
        del self.map[val]
        self.array.pop()
        return True
    
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.array) - 1)
        return self.array[idx]

