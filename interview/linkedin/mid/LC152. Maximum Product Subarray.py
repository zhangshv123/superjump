"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.


"""
"""
最开始时，设置当前当前最大值和最小值均为1，最终最大值为数组第一个数字，还要定义一个oldMaxIdx变量来保存之前最大值，然后最每一个遍历的数字根据其正负分别做不同的处理：

1. 当遍历到一个正数时，此时的最大值等于之前的最大值乘以这个正数，此时的最小值等于它本身再乘以这个正数。

2. 当遍历到一个负数时，此时的最大值等于之前最小值乘以这个负数，这时候问题就来了，挖掘技术哪家强？哈哈，言归正传，这时候问题就来了，当之前的最小值是负数时，负负得正没有问题，当之前的最小值是正数时，在乘以一个负数，当前最大值就变成负数了，这怎么办，没关系，在下次循环时，会和1比较取大的，负数就被舍弃了，程序继续正常执行。此时的最小值等于之前最大值（肯定是正数）乘以这个负数，还是负数。

3. 在每遍历完一个数时，都要更新最终的最大值。

Besides keeping track of the largest product, we also need to keep track of the smallest product. Why? The smallest product, which is the largest in the negative sense could become the maximum when being multiplied by a negative number.

Let us denote that:

f(k) = Largest product subarray, from index 0 up to k.
 

Similarly,

g(k) = Smallest product subarray, from index 0 up to k.
 

Then,

f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )
g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )
 

There we have a dynamic programming formula. Using two arrays of size n, we could deduce the final answer as f(n-1). Since we only need to access its previous elements at each step, two variables are sufficient.
所有求substring，subarray， 最大最小都转化为以i为结尾的最大最小，
然后对于所有以i为最大最小的出的结论里遍历得到原问题的最大最小

"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #largest, smallest-> contains current num
        max_cur, min_cur, max_sofar = 1, 1, -sys.maxint
        for num in nums:
            max_cur, min_cur = max(num, num * max_cur, num * min_cur), min(num, num * max_cur, num * min_cur)
            max_sofar = max(max_sofar, max_cur)
        return max_sofar
