"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
"""
class Solution(object):
    def getParent(self, s, p):
        if p[s] == s:
            return s
        else:
            return self.getParent(p[s], p)
    def union(self, s1, s2, p):
        p1, p2 = self.getParent(s1, p), self.getParent(s2, p)
        p[p1] = p2
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parents, count = {}, 0
        n = len(M)
        for i in range(n):
            parents[i] = i
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(i, j, parents)
        return sum(map(lambda i: 1 if parents[i] == i else 0, range(n)))


