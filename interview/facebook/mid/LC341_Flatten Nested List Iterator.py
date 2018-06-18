#!/usr/bin/python
"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Show Company Tags
Show Tags
Show Similar Problems

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
todo: top solution
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stk = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        s = self.stk
        nl, idx = s[-1]
        s[-1][1] += 1
        return nl[idx].getInteger()
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stk
        while len(s) > 0:
            nl, idx = s[-1]
            if len(nl) == idx:
                s.pop()
            else:
                x = nl[idx]
                if x.isInteger():
                    return True
                else:
                    s[-1][1] += 1
                    s.append([x.getList(), 0])                    
        return False
        
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

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())