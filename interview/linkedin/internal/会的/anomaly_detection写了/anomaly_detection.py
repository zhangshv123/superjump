def findMaxAnomaly(arr, L):
	if not arr or L >= len(arr) or L == 0:
		raise Exception("invalid input")
	
	left, right = 0, L-1
	currentAve = currentAverage(arr, left, right)
	restAve = currentAverage(arr, right+1, len(arr) - 1)
	res = abs(currentAve - restAve)
	while right < len(arr) - 1:
		currentAve += (arr[right+1] - arr[left])/L
		restAve += (arr[left] - arr[right+1])/(len(arr) - L)
		right += 1
		left += 1
		if abs(currentAve - restAve) > res:
			res = abs(currentAve - restAve)
	return res
	

def currentAverage(arr, start, end):
	total = 0
	for i in range(start, end+1):
		total += arr[i]
	return total/(end - start + 1)

print findMaxAnomaly([1.0, 1.1, 5.5, 4.5, 0.9], 2)
print findMaxAnomaly([1.0, -5.0, 0.0, -2.5, 1.2], 3)
	

