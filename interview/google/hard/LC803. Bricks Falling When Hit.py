"""
We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input: 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation: 
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Example 2:
Input: 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: 
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
"""
# https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back

class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])
        
        # Connect unconnected bricks and 
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j]!=1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += sum(dfs(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            return ret
        
        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
                
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j]==1 and is_connected(i, j):
                ret[k] = dfs(i, j)-1
            
        return ret