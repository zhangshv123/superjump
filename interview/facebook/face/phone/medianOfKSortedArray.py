# 给M个sorted array，求median
import heapq
def medianOfKsortedArray(arrs):
    h = []
    for arr in arrs:
        heapq.heappush(h, (arr[0], 0, arr))
    m = []
    while len(h) > 0:
        val, idx, arr = heapq.heappop(h)
        m.append(val)
        idx += 1
        if idx < len(arr):
            heapq.heappush(h, (arr[idx], idx, arr))
    return m[int(len(m) / 2)]
print(medianOfKsortedArray([[1,5,9],[4,6,8],[2,3,7]]))


import heapq
def medianOfKsortedArray(arrs):
    def bs(arr, t):
        i, j = 0, len(arr)
        while i < j:
            m = (j - i) / 2 + i
            if arr[m] <= t:
                i = m + 1
            else:
                j = m - 1
        return j + 1
    i, j, l = min(min(arrs)), max(max(arrs)), sum(map(lambda a: len(a), arrs))
    while i < j:
        m = (j - i) / 2 + i
        print(map(lambda arr: bs(arr, m), arrs), m, i, j)
        if sum(map(lambda arr: bs(arr, m), arrs)) <= l / 2:
            i = m + 1
        else:
            j = m - 1
    return j
print(medianOfKsortedArray([[1,5,9],[4,6,8],[2,3,7]]))