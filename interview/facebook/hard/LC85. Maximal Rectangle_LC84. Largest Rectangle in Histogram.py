"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""
"""
借助上一题 Largest Rectangle in Histogram 的解法。

我们现在把矩阵的每一行当做是上一题的问题，然后遍历所有的行数，取最大数就是解。

这里的每一行的高度怎么确定呢。

1.如果当前点为‘0’，那么高度就是0

2.如果当前点为‘1’，那么高度就是往上连续1的个数（包括自己）。

求高度是一个动态规划过程。用dp[i][j]来存某个位置的高度那么
"""
class Solution(object):  
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]] int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        heights = [0 for _ in range(len(matrix[0]))]
        max_area = 0
        for row in matrix:
            #update the heights
            for i, item in enumerate(row):
                heights[i] = 0 if item == "0" else heights[i] + 1
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area


"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.
For example,
Given heights = [2,1,5,6,2,3],
return 10.
这道题目算是比较难得一道题目了，首先最简单的做法就是对于任意一个bar，向左向右遍历，直到高度小于该bar，这时候计算该区域
的矩形区域面积。对于每一个bar，我们都做如上处理，最后就可以得到最大值了。当然这种做法是O(n2)，铁定过不了大数据集合测试的。

从上面我们直到，对于任意一个bar n，我们得到的包含该bar n的矩形区域里面bar n是最小的。我们使用ln和rn来表示bar 
n向左以及向右第一个小于bar n的bar的索引位置。

譬如题目中的bar 2的高度为5，它的ln为1，rn为4。包含bar 2的矩形区域面积为(4 - 1 - 1) * 5 = 10。

我们可以从左到右遍历所有bar，并将其push到一个stack中，如果当前bar的高度小于栈顶bar，我们pop出栈顶的bar，
同时以该bar计算矩形面积。那么我们如何知道该bar的ln和rn呢？rn铁定就是当前遍历到的bar的索引，而ln则是当前的栈顶bar的索引，
因为此时栈顶bar的高度一定小于pop出来的bar的高度。

为了更好的处理最后一个bar的情况，我们在实际中会插入一个高度为0的bar，这样就能pop出最后一个bar并计算了。
"""
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stk = []
        area = 0
        heights.append(0)
        for i, height in enumerate(heights):
            #pop ele larger than height from end of stk
            while len(stk) > 0 and height <= heights[stk[-1]]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1 if len(stk) != 0 else i
                area = max(area, h * w)
            stk.append(i)
        heights.pop()
        return area         


        