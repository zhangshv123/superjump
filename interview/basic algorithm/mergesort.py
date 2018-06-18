版本一：
def msort2(x):
	if len(x) < 2:
		return x
	result = []          # moved!
	mid = int(len(x)/2)
	y = msort2(x[:mid])
	z = msort2(x[mid:])
	while (len(y) > 0) and (len(z) > 0):
			if y[0] > z[0]:
				result.append(z[0])
				z.pop(0)
			else:
				result.append(y[0])
				y.pop(0)
	result += y
	result += z
	return result
版本二：用Index代替pop
def msort3(x):
	result = []
	if len(x) < 2:
		return x
	mid = int(len(x)/2)
	y = msort3(x[:mid])
	z = msort3(x[mid:])
	i = 0
	j = 0
	while i < len(y) and j < len(z):
			if y[i] > z[j]:
				result.append(z[j])
				j += 1
			else:
				result.append(y[i])
				i += 1
	result += y[i:]
	result += z[j:]
	return result
版本三:当数量小于20用built的非recursive版本
def msort4(x):
	result = []
	if len(x) < 20:
		return sorted(x)
	mid = int(len(x)/2)
	y = msort4(x[:mid])
	z = msort4(x[mid:])
	i = 0
	j = 0
	while i < len(y) and j < len(z):
			if y[i] > z[j]:
				result.append(z[j])
				j += 1
			else:
				result.append(y[i])
				i += 1
	result += y[i:]
	result += z[j:]
	return result
print(msort3([1,3,2]))