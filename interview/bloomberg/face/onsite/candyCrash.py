#!/usr/bin/python
def candyCrash(arr):
	i = 0
	a = list(arr)
	for j in range(len(arr) + 1):
		if (j == len(arr) or a[j] != a[i]) and j - i > 2:
			a[i: j] = ["#"] * (j - i)
			i = j
	return "".join(a)
print(candyCrash("aaaabb"))
	