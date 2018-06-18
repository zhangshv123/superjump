#http://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/
# Given an almost sorted array where only two elements are swapped, 
# how to sort the array efficiently?

# Example

# Input:  arr[] = {10, 20, 60, 40, 50, 30}  
# // 30 and 60 are swapped
# Output: arr[] = {10, 20, 30, 40, 50, 60}

# Input:  arr[] = {10, 20, 40, 30, 50, 60}  
# // 30 and 40 are swapped
# Output: arr[] = {10, 20, 30, 40, 50, 60}

# Input:   arr[] = {1, 5, 3}
# // 3 and 5 are swapped
# Output:  arr[] = {1, 3, 5}

def sortByOneSwap(nums):
	n = len(nums)
	for i in range(n-1,0,-1):
		if nums[i] < nums[i-1]:
			j = i - 1
			while j>=0 and nums[i] < nums[j]:
				j -=1
		
			nums[i],nums[j+1] = nums[j+1],nums[i]
			break
	return nums

print sortByOneSwap([1,2,6,4,5,3,10,20,60,40,50,30])
			
