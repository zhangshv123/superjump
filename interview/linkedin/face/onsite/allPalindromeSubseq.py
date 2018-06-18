"""
找出字符串中所有的回文subsequence not substring。（LC516变型）
当时讨论的解法就是，看两头的字母，如果不相同，这两个字母肯定不可能同时存在于最后的某个答案中。
所以要么去掉左边字符，要么去掉右边字符，继续搜索。但如果两边字符相同，就去掉头和尾巴。
因为这里sub problem 有很多重复。但是这个解看似可以cache,但是每次在merge答案的时候还是有时间开销。
worst case个人觉得和暴力解法相同。
LC730
"""
from collections import defaultdict
class Solution(object):
    def allPalindromeSubseq(self, s):
        dp = defaultdict(set)
        def dfs(i, j):
            if i > j:
                return {""}
            if i == j:
                return {s[i]}
            if (i, j) in dp:
                return dp[i, j]        
            if s[i] == s[j]:
                mid = dfs(i + 1, j - 1)
                dp[i, j] |= mid
                for m in mid:
                    dp[i, j].add(s[i] + m + s[j])
                dp[i, j] |= {s[i], s[j], s[i] + s[j]}    
            else:
                dp[i, j] = dfs(i, j - 1) | dfs(i + 1, j)
            return dp[i, j]   
        return len(list(dfs(0, len(s) - 1) - {""}))

d = Solution()
print(d.allPalindromeSubseq("bbbab"))