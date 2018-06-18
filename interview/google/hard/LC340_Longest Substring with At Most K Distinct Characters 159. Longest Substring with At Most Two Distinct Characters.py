"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""
"""
讲解先可以说naive o(n^2)，然后说优化成双指针
变成以j为结尾的最优解，遍历所有j的情况找答案最优
#双指针的题目完全可以用存在sol和不存在sol来分类,写思路写细一些，写代码不容易反复修改
（i, j）因为 如果
1, 4 n -> 1, 5 n  如果1-4都超过k个，那么1-5肯定超过k个，不用从头走一遍
2, 4 n -> 2, 5 n
3, 4 y  
所以当 j到5 的时候i不用回头从1开始而是继续在3就可以
关键在于：
外层指针依然是依次遍历
内层指针证明是否需要回退
substring i ~ j
对所有f(j) = i， 代表以j为起点最小的i，满足题意, 答案为 max(f(j)) j: 0 -> n - 1

GG follow up
面试官说数据是steam进来的，内存存不下。想用 priority dictionary解，面试官让实现 priority dictionary，lz这里做的不好，之前没有想过priority dictionary的实现，只能现场想。最后，面试官说很接近了，给了hint解决。

"""
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charMap = defaultdict(int)
        left, right, max_length = 0, 0, 0
        while right < len(s):
            charMap[s[right]] += 1
            while len(charMap) > k:
                charMap[s[left]] -= 1
                if charMap[s[left]] == 0:
                    del charMap[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
        

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s)
        return lengthOfLongestSubstringKDistinct(self, s, 2)