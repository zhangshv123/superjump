# 给一个整数数组 int[] nums, 要判断是否存在这样一个pair, |i- j| > k, nums + nums[j] = M, k 和M都是给定的， 返回一个boolean
def f(nums, k, M):
    m = {}
    for i, num in enumerate(nums):
        if M - num in m and i - m[M - num] > k:
            return True
        m[num] = i
    return False
#print(f([1, 2, 3, 4, 5, 6], 5, 7))

#要找一个最长的subsequence, 这个subsequence中间只能有一次下降，其余的都要递增
def g(nums):
    dec = [0]
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            dec.append(i)
    dec.append(len(nums))
    res = -1
    for i in range(2, len(dec)):
        res = max(res, dec[i] - dec[i - 2])
    return res if res != -1 else len(nums)
print(g([0,1,3,2,5,4,9,6]))
        
    