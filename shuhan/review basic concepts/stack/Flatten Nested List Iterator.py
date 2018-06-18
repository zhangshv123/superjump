# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator(object):
    nums = deque()
    index = 0
    def flatten(self, nested_integer):
        if nested_integer.isInteger():
            return [nested_integer.getInteger()]
        else:
            res = []
            for sub_nested_integer in nested_integer.getList():
                res += self.flatten(sub_nested_integer)
            return res
    def __init__(self, nestedList):
        # Initialize your data structure here.
        for nested_integer in nestedList:
            self.nums += self.flatten(nested_integer)
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.nums.popleft()
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return len(self.nums) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())