#Intersection of two sorted interval lists, A=[(1,2), (5,7)..] B=[(2,6)...]  return [(5,6)..]

def getIntersections(l, r):
	points = []
	for s, e in l + r:
		points.append((s, 1))
		points.append((e, -1))
	points.sort(lambda a, b: a[1] - b[1] if a[0] == b[0] else a[0] - b[0])
	res, score, start = [], 0, 0
	for p in points:
		score += p[1]
		if p[1] == 1 and score == 2:
			start = p[0]
		if p[1] == -1 and score == 1:
			res.append((start, p[0]))
	return res
l = [[1, 2], [5, 7], [9, 10], [11, 12], [13, 14]]
r = [[2,6], [8, 17]]	
print getIntersections(l, r)
		