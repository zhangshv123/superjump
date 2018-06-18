"""

Why did I use s binary search?
In fact there are some similar problems on Leetcode so that is part of experience.
Secondly, I got a hint from “Answers within 10^-6 of the true value will be accepted as correct.”. The first solution I tried was binary search.
Because binary search may not find exact value but it can approach the true answer.

Explanation of solution
Now we are using binary search to find the smallest possible value of D.
I initilze left = 0 and right = the distance between the first and the last station
count is the number of gas station we need to make it possible.
if count > K, it means mid is too small to realize using only K more stations.
if count <= K, it means mid is possible and we can continue to find a bigger one.
When left + 1e-6 >= right, it means the answer within 10^-6 of the true value and it will be accepted.
"""
def minmaxGasDist(self, st, K):
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right