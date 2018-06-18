"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""
"""
这道题给了我们一个正整数n，让我们写出所有的因子相乘的形式，而且规定了因子从小到大的顺序排列，
那么对于这种需要列出所有的情况的题目，通常都是用回溯法来求解的，由于题目中说明了1和n本身不能算其因子，
那么我们可以从2开始遍历到n，如果当前的数i可以被n整除，说明i是n的一个因子，我们将其存入一位数组out中，
然后递归调用n/i，此时不从2开始遍历，而是从i遍历到n/i，停止的条件是当n等于1时，如果此时out中有因子，
我们将这个组合存入结果res中
我们仔细观察题目中给的两个例子的结果，可以发现每个组合的第一个数字都没有超过n的平方根，这个也很好理解，
由于要求序列是从小到大排列的，那么如果第一个数字大于了n的平方根，而且n本身又不算因子，那么后面那个因子
也必然要与n的平方根，这样乘起来就必然会超过n，所以不会出现这种情况。那么我们刚开始在2到n的平方根之间
进行遍历，如果遇到因子，先复制原来的一位数组out为一个新的一位数组new_out，然后把此因子i加入new_out，
然后再递归调用n/i，并且从i遍历到n/i的平方根，之后再把n/i放入new_out，并且存入结果res，由于层层迭代的调用，
凡是本身能继续拆分成更小因数的都能在之后的迭代中拆分出来，并且加上之前结果，最终都会存res中
"""
import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, path = [], []
        self.dfs(2, n, path, res)
        return res
    
    def dfs(self, start, n, path, res):
        #base
        if len(path) > 0:
            res.append(path+ [n]) 
        #recursion
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                path.append(i)
                self.dfs(i, n / i, path, res)
                path.pop()

#用stk做dfs
import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, path, stk = [], [], []
        stk.append((2, n, -1))
        while len(stk) > 0:
            start, n, height = stk.pop()
            if len(path) <= height:
                path.append(start)
            elif height >= 0:
                path[height] = start
            #base
            if len(path) > 0:
                res.append(path[:height + 1] + [n]) 
            #recursion
            for i in range(start, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    path.append(i)
                    stk.append((i, n / i, height + 1))
                    path.pop()     
        return res                