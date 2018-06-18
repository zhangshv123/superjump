"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
"""
# get probablity of ended in each slot after K steps and add them
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dirc = [(-2, 1), (2, 1), (-2, -1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        dp = [[[0.0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
        dp[0][r][c] = 1
        for step in range(1, K + 1):
            for r in range(N):
                for c in range(N):
                    for di, dj in dirc:
                        x, y = di + r, dj + c
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        dp[step][r][c] += dp[step - 1][x][y] * 0.125
        return sum(map(lambda a: sum(a), dp[K]))

# memorization + dfs -> probablity of ending in board which started from r, c with init probability p to have k step
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dirc = [(-2, 1), (2, 1), (-2, -1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        dp = [[[0.0 for _ in range(N)] for _ in range(N)] for _ in range(K)]
        def dfs(r, c, p, k):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0.0
            if k == K:
                return p
            if dp[k][r][c] != 0.0:
                return dp[k][r][c]
            for dr, dc in dirc:
                dp[k][r][c] += dfs(r + dr, c + dc, p / 8, k + 1)
            return dp[k][r][c]
        return dfs(r, c, 1, 0)