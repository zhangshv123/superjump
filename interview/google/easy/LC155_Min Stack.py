"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
思路：
push
只有当minstack为空，或者x<=minstack才会放x进去mintack
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minStack = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.minStack[-1] == self.stk.pop():
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

2个 stk都插入东西的代码：
思路：
每次来一个东西，stk1,minstack都会插入，只是需要注意minstack为空，或者最小的已经没了。需要更新minV的情况
import sys
class MinStack(object):
    minV = sys.maxint
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stackMin = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        self.minV = min(self.minV, x)
        self.stackMin.append(self.minV)
        

    def pop(self):
        res = self.stack1.pop()
        self.stackMin.pop()
        if len(self.stackMin) == 0:
            self.minV = sys.maxint
        elif res < self.stackMin[-1]:
            self.minV = self.stackMin[-1]
        
        return res

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stackMin[-1]
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()