"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n). 

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

双指针的题目完全可以用存在sol和不存在sol来分类
思路：思路很简单，就是遍历数组，先把所有的Ｔ中的字符找到，然后从左端缩减这个字符串，直到不能完全包含Ｔ．
但是实现起来还是需要一些技巧．因为时间复杂度限制在了O(n)，所以需要在O(1)的时间内判断是不是找到了所有
的Ｔ中的字符．可以用一个hash表来计数所有字符出现的次数和一个标记num代表Ｔ总共有多少字符．

然后遍历S，并且将当前字符在hash表中计数减一，如果当前字符在hash表中计数是大于０的，
说明这个字符是出现在Ｔ中的，将num也减一，代表我们找到了一个（这个num就是总共有多少字符，
我们需要这个来标记是不是找完了所有字符，这也是能够在O(1)时间内判断当前窗口是不是覆盖了Ｔ的关键）．
这样当总的数量为０的时候我们就找到了一个覆盖Ｔ的子串窗口．这个窗口因为左端可能包含了一些不必要的字符，
因此我们需要将窗口的左端向右移动，使其正好包含Ｔ．在窗口左端向右移动的过程中需要将碰到字符在hash表中
＋１，如果当前字符在hash表中的计数为０，而且我们又碰到了，说明这个字符是出现在Ｔ中的，因此num要加一．
"""
"""
#双指针的题目完全可以用存在sol和不存在sol来分类
讲解先可以说naive o(n^2)，然后说优化
（i, j）因为 如果
f:i, j move 
g: fix j, i could move
f: min(g(0->n-1))
1, 4 y  -> 1, 5 y  1,4满足 ->1,5肯定满足，但肯定没有1，4短  
2, 4 y  -> 2, 5 y  2,4满足 ->2,5肯定满足，但肯定没有2，4短  
3, 4 n  -> 3, 5 ?
所以当 j到5 的时候y不用回头从1开始而是继续在3就可以

关键在于：
外层指针依然是依次遍历
内层指针证明是否需要回退

当存在sol，通过移动右指针找最优sol
当不存在sol，通过移动左指针达到sol
"""
#FB说时间复杂度 O(2n + m)worst case，意思是还要考虑把mapT元素加进去的时间
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needNum, needMap = len(t), defaultdict(int)
        for c in t:
            needMap[c] += 1
        left, right, res = 0, 0, s + t
        while right < len(s):
            if needMap[s[right]] > 0:
                needNum -= 1
            needMap[s[right]] -= 1
            while needNum == 0:
                #update sol
                if len(res) > right - left + 1:
                    res = s[left: right + 1]
                if needMap[s[left]] == 0:
                    needNum += 1
                needMap[s[left]] += 1
                left += 1
            right += 1
        return res if res != s + t else ""
                