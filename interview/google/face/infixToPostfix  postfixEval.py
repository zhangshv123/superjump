"""
前缀表达式转后缀，要求O（1）空间复杂度
"""
# http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
"""

Infix Expression        Prefix Expression        Postfix Expression
A + B * C + D        + + A * B C D        A B C * + D +
(A + B) * (C + D)        * + A B + C D        A B + C D + *
A * B + C * D        + * A B * C D        A B * C D * +
A + B + C + D        + + + A B C D        A B + C + D +

1.Create an empty stack called opstack for keeping operators. Create an empty list for output.
2.Convert the input infix string to a list by using the string method split.
3.Scan the token list from left to right.
    a.If the token is an operand, append it to the end of the output list.
    b.If the token is a left parenthesis, push it on the opstack.
    c.If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. 
    Append each operator to the end of the output list.
    d.If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators 
    already on the opstack that have higher or equal precedence and append them to the output list.
4.When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
"""
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))



from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))