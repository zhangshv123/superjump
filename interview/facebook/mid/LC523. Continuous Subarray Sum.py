我们定义一个哈希表，用来保存截止目前的和模k之后的余数，例如截止i的时候，哈希表里面有2,3两个数，那么就表示扫描到nums[i]的时候，前面的和模k之后的余数有2,3。
那么当我们扫描到j >= i + 2或者之后，如果发现截止当前的和模k的余数已经在哈希表里面了，就说明从[i + 1, j]这个闭区间的数的和可以被k整除。

一般情况下，我们可以用一个unordered_map，顺便把索引也保存一下，这样便于判断两个索引的差值是不是大于等于2。但是在下面的代码片段里面我们用了一个过渡变量pre，也就是扫描到当前位置的时候，我们才插入前一个余数pre，这样其实只需要一个unordered_set就可以了。

算法的时间复杂度是O(n)，空间复杂度是O(k)，因为hash表的大小的最大可能值就是k。
from sets import Set
class Solution(object):
	def checkSubarraySum(self, nums, k):
		total, pre = 0, 0
		s = set()
		for i in range(len(nums)):
			total += nums[i]
			total = total if k == 0 else total%k
			if total in s:
				return True
			s.add(pre)
			pre = total
		return False
			
		

s = Solution()
print s.checkSubarraySum([0,1,0,0],0)
			
follow up:
如果resize page,col发生变换了，怎么办？
先按照 exist/new col，然后平铺， 铺完了，继续用原来的方法放			
			
			
			