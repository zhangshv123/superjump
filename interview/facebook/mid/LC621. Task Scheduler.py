"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
from collections import defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        m = max(d.values())
        c = len(filter(lambda a: a == m, d.values()))
        return max(len(tasks), (m - 1) * (n + 1) + c)

"""
原题：
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

新的就是不能换order：
A idle idle A idle idle A idle idle A  B  idle idle  B  idle idle B

1.A not in d
2.A in d, not need " "
3.A in d, need " "

1, 2 could combine
"""        
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        i = 0
        for t in tasks:
            if t in d and i - d[t] < n:
                i = d[t] + n + 1
            else:
                i += 1
            d[t] = i
        return i
s = Solution()
print s.leastInterval(['A','A','A','B','B','B'], 2)        