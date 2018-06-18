#这个是greedy，只能返回一个结果(hard的LC301是返回所有的)，一定是最短的
class Solution(object):
    def longestValidParentheses(self, s):
        stk, remove = [], []
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            if c == ")":
                if len(stk) > 0:
                    stk.pop()
                else:
                    remove.append(i)
        remove += stk
        res = ""
        for i, c in enumerate(s):
            if i not in remove:
                res += c
        return res
s = Solution()
print s.longestValidParentheses("()())()")
print s.longestValidParentheses("(")
                
                          