#!/usr/bin/python
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""
"""
Keep a global running total and a stack of signs (+1 or -1), one for each open scope. The “global” outermost sign is +1.

Each number consumes a sign.
Each + and - causes a new sign.
Each ( duplicates the current sign so it can be used for the first term inside the new scope. That’s also why I start
 with [1, 1] - the global sign 1 and a duplicate to be used for the first term, since expressions start like 3... 
 or (..., not like +3... or +(....
Each ) closes the current scope and thus drops the current sign.
"""

"""
Example trace:

Here’s an example trace for input 3-(2+(9-4)).

  remaining   sign stack      total
3-(2+(9-4))   [1, 1]            0
 -(2+(9-4))   [1]               3
  (2+(9-4))   [1, -1]           3
   2+(9-4))   [1, -1, -1]       3
    +(9-4))   [1, -1]           1
     (9-4))   [1, -1, -1]       1
      9-4))   [1, -1, -1, -1]   1
       -4))   [1, -1, -1]      -8
        4))   [1, -1, -1, 1]   -8
         ))   [1, -1, -1]      -4
          )   [1, -1]          -4
              [1]              -4
If you want to see traces for other examples, you can add this at the start inside the loop and after the loop 
(that’s for the Python solution, where it’s all easier):

print '%11s   %-16s %2d' % (s[i:], signs, total)
"""

class Solution:
    def calculate(self, s):
        res = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start: i])
            else:
                if s[i] in "+-(":
                    signs.append(signs[-1] * (1, -1)[s[i] == "-"])
                elif s[i] == ")":
                    signs.pop()
                i += 1
        return res

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, sign, stk = 0, "+", []
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                if sign == "+":
                    stk.append(int(s[start: i]))
                elif sign == "-":
                    stk.append(-int(s[start: i]))
                elif sign == "*":
                    stk.append(stk.pop() * int(s[start: i]))
                elif sign == "/":
                    stk.append(int(stk.pop() / int(s[start: i])))
            elif s[i] in "+-*/":
                sign = s[i]
                i += 1
            else:
                i += 1
        return sum(stk)
                       
                