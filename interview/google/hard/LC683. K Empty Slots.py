"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
"""
# 循环每一天，然后开花，然后检查新开花位置两边距离各多少，更新hashset。

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        gardens = [False] * n
        for i in range(n):
            x = flowers[i] - 1
            gardens[x] = True
            for dx in [-1, 1]:
                xx = x + dx
                while xx >= 0 and xx < n:
                    if gardens[xx]:
                        if abs(xx - x) - 1 == k:
                            return i + 1
                        break
                    xx += dx
        return -1

        
class Solution(object):
	def kEmptySlots(self, flowers, k):
		n = len(flowers)
		garden = [False] * n
		d = set()
		# iterate through day
		i = 0
		while i < n:
			x = flowers[i] - 1
			garden[x] = True
			# iterate through flowers
			left = 1
			right = 1
			while x - left >= 0:
				if garden[x - left]:
					d.add(left - 1)
					break
				left += 1
			while x + right < n:
				if garden[x + right]:
					d.add(right - 1)
					break
				right += 1
			if k in d:
				return i + 1
			i += 1
		return -1

#BST treeset
"""
public int kEmptySlots(int[] flowers, int k) {
	TreeSet<Integer> treeSet = new TreeSet<>();
	for (int i = 0; i < flowers.length; i++) {
		int current = flowers[i];
		Integer next = treeSet.higher(current);
		if (next != null && next - current == k + 1) {
			return i + 1;
		}
		Integer pre = treeSet.lower(current);
		if (pre != null && current - pre == k + 1) {
			return i + 1;
		}
		treeSet.add(current);
	}
	return -1;
}
""" 


"""
小变形
就是说给你一个k，如果这一排里面有任意一组连续的几朵花长度是k，即满足要求。不过它问的是最后一天满足这个要求的天数。



解法倒是不难，我是按照lc的解法改了改，把天数从后往前遍历的，当做每天有一朵花要收起来，然后把现在的empty slot
当做是原版题里面的花，把花当做原版里面empty slots。这个做法有一个要特别注意的地方：原版里面的empty slots
要求两边都有花夹住这一组empty slots，但是这道题里面如果有连续k朵花是从墙开始数的，那么这个是要算成符合要求的。
所以你要想办法把这个改动解决掉。
"""
