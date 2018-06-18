"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""
# https://leetcode.com/problems/bomb-enemy/discuss/83387/Short-O(mn)-time-O(n)-space-solution
"""
比较naive的做法是每个空位都向前后左右搜索, 但是这样的搜索包含了大量的重复搜索, 所以如何利用已经搜索过的信息就是本题的考点了. 
对于每一行来说, 我们可以在第0列或者当前位置前一列为墙的时候从第当前列开始往右搜索直到撞到墙. 对于每一列来说, 
可以在第0行的时候或者在当前行前一行为墙的时候从当前行往下搜索, 直到碰到墙为止. 这样就可以一次计算出一行直到碰到墙之前有几个敌人, 
一列在没有碰到墙之前有几个敌人. 直到当某个某位之前位置墙的时候才会重新计算. 
"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        m, n = len(grid), 0 if len(grid) == 0 else len(grid[0])
        res, rowhits, colhits = 0, 0, [0] * n
        for i in range(m):
            for j in range(n):
                if not j or grid[i][j - 1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        rowhits += grid[i][k] == 'E'
                        k += 1
                if not i or grid[i - 1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colhits[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, rowhits + colhits[j])
        return res

"""
这道题相当于一个简单的炸弹人游戏，让我想起了小时候玩的红白机的炸弹人游戏，放一个炸弹，然后爆炸后会炸出个‘十’字，上下左右的东西都炸掉了。
这道题是个简化版，字母E代表敌人，W代表墙壁，这里说明了炸弹无法炸穿墙壁。数字0表示可以放炸弹的位置，让我们找出一个放炸弹的位置可以炸死最多的敌人。
那么我最开始想出的方法是建立四个累加数组v1, v2, v3, v4，其中v1是水平方向从左到右的累加数组，v2是水平方向从右到左的累加数组，v3是竖直方向
从上到下的累加数组，v4是竖直方向从下到上的累加数组，我们建立好这个累加数组后，对于任意位置(i, j)，其可以炸死的最多敌人数就是v1[i][j] + 
v2[i][j] + v3[i][j] + v4[i][j]，最后我们通过比较每个位置的累加和，就可以得到结果
"""
import copy
class Solution(object):
    def maxKilledEnemies(self, grid):
        m, n = len(grid), 0 if len(grid) == 0 else len(grid[0])
        res = 0
        v1 = [[0 for j in range(n)] for i in range(m)]
        v2, v3, v4 = copy.deepcopy(v1), copy.deepcopy(v1), copy.deepcopy(v1)
        for i in range(m):
            for j in range(n):
                t = 0 if (j == 0 or grid[i][j] == 'W') else v1[i][j - 1]
                v1[i][j] = t + 1 if grid[i][j] == 'E' else t
            for j in reversed(range(n)):
                t = 0 if (j == n - 1 or grid[i][j] == 'W') else v2[i][j + 1]
                v2[i][j] = t + 1 if grid[i][j] == 'E' else t
        for j in range(n):
            for i in range(m):
                t = 0 if (i == 0 or grid[i][j] == 'W') else v3[i - 1][j]
                v3[i][j] = t + 1 if grid[i][j] == 'E' else t
            for i in reversed(range(m)):
                t = 0 if (i == m - 1 or grid[i][j] == 'W') else v4[i + 1][j]
                v4[i][j] = t + 1 if grid[i][j] == 'E' else t
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j])
        return res        