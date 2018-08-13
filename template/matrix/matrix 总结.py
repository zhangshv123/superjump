matrix 总结
1.给一个N*N 的matrix, 找到里面sum最大的一个sub matrix
naive的解法是O(N^5)
因为i, j, size, sum up 对应的复杂度是:
O(n * n * n * n^2) = O(N^5)
 DP的解法：
dp[i][j][step] 代表以i,j为左上方起点，长度为step的matrix 的subsum
时间复杂度：
因为从dp[i][j][step - 1] 变成dp[i][j][step]需要O(n)的时间
所以时间复杂度是O(n^4)

2. 给一个N*N 的matrix, 找到里面只包含1的最大的一个sub matrix
https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
dp[i][j] 代表i,j作为右下角的终点的matrix，最长的全1矩阵的边长
时间复杂度：
O(N^2)
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
