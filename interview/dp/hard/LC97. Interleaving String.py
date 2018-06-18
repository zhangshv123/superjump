"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
"""
首先，这道题的大前提是字符串s1和s2的长度和必须等于s3的长度，如果不等于，肯定返回false。那么当s1和s2是空串的时候，s3必然是空串，则返回true。
所以直接给dp[0][0]赋值true，然后若s1和s2其中的一个为空串的话，那么另一个肯定和s3的长度相等，则按位比较，若相同且上一个位置为True，赋True，
其余情况都赋False，这样的二维数组dp的边缘就初始化好了。下面只需要找出递推公式来更新整个数组即可，我们发现，在任意非边缘位置dp[i][j]时，
它的左边或上边有可能为True或是False，两边都可以更新过来，只要有一条路通着，那么这个点就可以为True。那么我们得分别来看，如果左边的为True，
那么我们去除当前对应的s2中的字符串s2[j - 1] 和 s3中对应的位置的字符相比（计算对应位置时还要考虑已匹配的s1中的字符），为s3[j - 1 + i], 
如果相等，则赋True，反之赋False。 而上边为True的情况也类似，所以可以求出递推公式为：

dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        # dp[i][j]: s1[:i], s2[:j], s3[:i+j]子问题
        dp = [False for _ in range(n + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0 and j <= n:
                    dp[j] = s2[j - 1] == s3[j - 1] and dp[j - 1]
                elif i <= m and j == 0:
                    dp[j] = s1[i - 1] == s3[i - 1] and dp[j]
                else:
                    dp[j] = (s1[i - 1] == s3[i + j - 1] and dp[j]) or (s2[j - 1] == s3[i + j - 1] and dp[j - 1])
        return dp[n]