"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
sol 1
利用每一层将当前整数加起来，
然后往后遍历多一层就将前面已经加过的数再加一遍．非常巧妙!
/_\ +  /\  +    /\
      /__\     /  \
              /____\
"""
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        unweighted, weighted = 0, 0
        #bfs
        while len(nestedList) > 0:
            nextLevel = []
            levelSum = 0
            for ni in nestedList:
                if ni.isInteger():
                    levelSum += ni.getInteger()
                else:
                    for nj in ni.getList():
                        nextLevel.append(nj)
            unweighted += levelSum
            weighted += unweighted
            nestedList = nextLevel
        return weighted
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = 0
        #bfs
        q = deque()
        hasNextLevel = False
        sub_nestedList = []
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                res += nestedInteger.getInteger()
                sub_nestedList.append(nestedInteger)
            else:
                sub_nestedList += nestedInteger.getList()
                hasNextLevel = True
        if hasNextLevel:
            res += self.depthSumInverse(sub_nestedList)
        return res

# 非recursion的做法，更普遍：
# 先把同一层的加和，最后再乘以level，这里的level是(len(tot) - i + 1)
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        tot = []
        self.helper(nestedList, 0, tot)
        sum = 0
        for i in xrange(0, len(tot)):
            sum += tot[i] * (len(tot) - i + 1)
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
        