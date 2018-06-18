class Solution(object):
	def decodeString(self, s):
		stack = []; curNum = 0; curString = ''
		for c in s:
			if c == '[':
				stack.append(curString)
				stack.append(curNum)
				curString = ''
				curNum = 0
			elif c == ']':
				num = stack.pop()
				prevString = stack.pop()
				curString = prevString + num*curString
			elif c.isdigit():
				curNum = curNum*10 + int(c)
			else:
				curString += c
		return curString
"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution(object): 
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curNum, curS, stk = "", "", []
        for c in s:
            if c.isdigit():
                curNum += c
            elif c.isalpha():
                curS += c
            if c == "[":
                stk.append(curS)
                stk.append(curNum)
                curNum, curS = "", ""
            if c == "]":
                num, preS = int(stk.pop()), stk.pop()
                curS = preS + num * curS
        return curS
s = Solution()
print s.decodeString("3[a2[c]]")
"""
follow up 是给你一个压缩好的字符串和一个位置（解压缩以后的偏移位置），让你返回该位置的字符 -》最后十几分钟，没有写代码 口述： 用一个辅助函数算子串解压缩以后的长度，然后和偏移下标做模运算，算出子串里对应的偏移量，然后递归。 感觉这个可以优化一下，因为算长度的函数会在一个子串上重复调用，也许可以用记忆化搜索吧。复杂度O(nlogn)。
举例子：
比如ab3[2[ef]cd]展开后是abefefcdefefcdefefcd 如果给你下标5你要返回f
"""