"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
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

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.helper(nestedList,1)
    
    def helper(self,lst,level):
        sum=0
        for item in lst:
            if item.isInteger():
                sum+=item.getInteger()*level
            else:
                sum+=self.helper(item.getList(),level+1)
        return sum

非recursion的做法，更普遍：
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        tot = []
        self.helper(nestedList, 0, tot)
        sum = 0
        for i in xrange(0, len(tot)):
            sum += tot[i] * (i + 1)
        return sum
    
    def helper(self, lst, height, tot):
        for c in lst:
            if c.isInteger():
                while height >= len(tot):
                    tot.append(0)
                tot[height] += c.getInteger()
            else:
                self.helper(c.getList(), height+1, tot)  
        return
    