"""

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
"""
我们提出维护量res[i][j][n]，其中i是s1的起始字符，j是s2的起始字符，而n是当前的字符串长度，res[i][j][len]表示的是以i和j分别为s1和s2起点的长度为len的字符串是不是互为scramble。
有了维护量我们接下来看看递推式，也就是怎么根据历史信息来得到res[i][j][len]。判断这个是不是满足，其实我们首先是把当前s1[i...i+len-1]字符串劈一刀分成两部分，然后分两种情况：
第一种是左边和s2[j...j+len-1]左边部分是不是scramble，以及右边和s2[j...j+len-1]右边部分是不是scramble；
第二种情况是左边和s2[j...j+len-1]右边部分是不是scramble，以及右边和s2[j...j+len-1]左边部分是不是scramble。
如果以上两种情况有一种成立，说明s1[i...i+len-1]和s2[j...j+len-1]是scramble的。而对于判断这些左右部分是不是scramble我们是有历史信息的，
因为长度小于n的所有情况我们都在前面求解过了（也就是长度是最外层循环）。
上面说的是劈一刀的情况，对于s1[i...i+len-1]我们有len-1种劈法，在这些劈法中只要有一种成立，那么两个串就是scramble的。
总结起来递推式是res[i][j][len] = || (res[i][j][k]&&res[i+k][j+k][len-k] || res[i][j+len-k][k]&&res[i+k][j][len-k]) 对于所有1<=k
如此总时间复杂度因为是三维动态规划，需要三层循环，加上每一步需要线行时间求解递推式，所以是O(n^4)。虽然已经比较高了，但是至少不是指数量级的，动态规划还是相当有用的，空间复杂度是O(n^3)。
"""
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        #dp[i][j][k]: s1[i:i + k], s2[j:j + k]子问题
        dp = [[[False for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        #按照长度走
        for k in range(1, n + 1):
            for i in range(n + 1 - k):
                for j in range(n + 1 - k):
                    if k == 1:
                        dp[i][j][k] = s1[i] == s2[j]
                    else:
                        q = 1
                        while q < k and not dp[i][j][k]:
                            dp[i][j][k] |= dp[i][j][q] and dp[i + q][j + q][k - q]
                            dp[i][j][k] |= dp[i][j + k - q][q] and dp[i + q][j][k - q]
                            q += 1
        return dp[0][0][n]