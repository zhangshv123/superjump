#public boolean canPlaceFlowers(List<Boolean> flowerbed, int numberToPlace)
#如果flowerbed当中为true，说明已经栽过花了，附近两个不能再栽花。numberToPlace代表想再栽多少花到flowerbed里。
#让return是不是还能栽那么多谢花进去。
from collections import deque
class Solution(object):
    def canPlaceFlowers(self,flowerbed, numberToPlace):
        for i in range(len(flowerbed)):
            if i != 0 and flowerbed[i - 1]:
                continue
            if flowerbed[i]:
                continue
            if i!= len(flowerbed) - 1 and flowerbed[i + 1]:
                continue
            flowerbed[i] = True
            numberToPlace -= 1
            if numberToPlace == 0:
                return True
        return False
        
s = Solution()
print s.canPlaceFlowers([True,False,True],2)