"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ? k ? n2.
"""
"""
首先将矩阵的左上角（下标0,0）元素加入堆

然后执行k次循环：

弹出堆顶元素top，记其下标为i, j

将其下方元素matrix[i + 1][j]，与右方元素matrix[i][j + 1]加入堆（若它们没有加入过堆）
"""
import sets
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = [(matrix[0][0], 0, 0)]
        direc = [(0, 1), (1, 0)]
        visited = set()
        for _ in range(k - 1):
            val, i, j = heapq.heappop(h)
            for di, dj in direc:
                ni, nj = i + di, j + dj
                if ni < len(matrix) and nj < len(matrix[0]) and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heapq.heappush(h, (matrix[ni][nj], ni, nj))
        return heapq.heappop(h)[0]
            
"""
上述解法的优化：

实际上visited数组可以省去，在队列扩展时，当且仅当j == 0时才向下扩展，否则只做横向扩展。
"""            
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans