"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
"""
#放回 true|false
#topological sort
1.collect in-degree
2.put all nodes that indegree = 0 into queue
3.bfs
from collections import defaultdict
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        outDegreeMap = defaultdict(list)
        inDegreeNum = defaultdict(int)
        for pre in prerequisites:
            outDegreeMap[pre[1]].append(pre[0])
            inDegreeNum[pre[0]] += 1
        q = []
        for c in range(numCourses):
            if inDegreeNum[c] == 0:
                q.append(c)
        index = 0
        while index < len(q):
            cur = q[index]
            index += 1
            for c in outDegreeMap[cur]:
                inDegreeNum[c] -= 1
                if inDegreeNum[c] == 0:
                    q.append(c)
        return len(q) == numCourses

#返回 排好序的答案
from collections import defaultdict
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        outDegreeMap = defaultdict(list)
        inDegreeNum = defaultdict(int)
        for pre in prerequisites:
            outDegreeMap[pre[1]].append(pre[0])
            inDegreeNum[pre[0]] += 1
        q = []
        for c in range(numCourses):
            if inDegreeNum[c] == 0:
                q.append(c)
        index = 0
        while index < len(q):
            cur = q[index]
            index += 1
            for c in outDegreeMap[cur]:
                inDegreeNum[c] -= 1
                if inDegreeNum[c] == 0:
                    q.append(c)
                    # follow up:
                    # if c == c1:
                    #     return len(q)
        return q if len(q) == numCourses else []
"""        
FB follow up:
    变种，返回  具体上到某节指定的课的时候，目前总共已经上了多少节了
    如果问的是在修2之前需要上多少门课的话，应该返回1。因为只需要上了0，就能上2了。
    所以说修完0的时候，你要看看下一步能不能去2，不能的话才去考虑与0连接的其他点，比如1。这样就能保证你肯定以最快的速度修到2.
"""    
    