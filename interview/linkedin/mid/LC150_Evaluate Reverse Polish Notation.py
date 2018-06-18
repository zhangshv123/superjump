#!/usr/bin/python
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

python: 6/(-132) = -1
in java, 6/(-132) = 0
so use int(operator.truediv(a, b)) or int(float(a)/b) etc. to be the same
"""
import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        ops = {"+" : operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token not in ops:
                stk.append(int(token))
            else:
                print stk, token
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(ops[token](num1, num2))
        return stk[0]

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
        return stack.pop()
        