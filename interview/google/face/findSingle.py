# int array, 所有數字都連著出現兩次，只有一個數字出現一次。找出只有一次的數字
def findSingle(input):
	res = 0
	for a in input:
		res ^= a
	return res
print findSingle([2, 2, 4, 4, 6])