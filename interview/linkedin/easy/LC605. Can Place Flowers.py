class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		for i in range(len(flowerbed)):
			if i != 0 and flowerbed[i - 1] == 1:  #不是第一个，并且前面有花
				continue
			if flowerbed[i] == 1: #如果当前位置有花
				continue
			if i!= len(flowerbed) - 1 and flowerbed[i + 1] == 1: #不是最后一个，并且后面有花
				continue
			flowerbed[i] = 1
			n -= 1
		return n <= 0