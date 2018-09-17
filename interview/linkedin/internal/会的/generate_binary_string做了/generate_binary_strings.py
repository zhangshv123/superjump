def generateBinary(n):
	res = []
	if n == 0:
		return [""]
	res = ["0","1"]
	firstHalf = []
	secondHalf = []
	for i in range(n-1):
		firstHalf = []
		secondHalf = []
		for j in res:
			firstHalf.append(j + "0")
			secondHalf.append(j + "1")
		secondHalf.reverse()
		firstHalf.extend(secondHalf)
		res = firstHalf
	return res

print generateBinary(3)

