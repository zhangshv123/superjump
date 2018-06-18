"""How to determine if three points are on the same line?

The answer is to see if slopes of arbitrary two pairs are the same.

Second, let's see what the minimum time complexity can be.

Definitely, O(n^2). It's because you have to calculate all slopes between any two points.

Then let's go back to the solution of this problem.

In order to make this discussion simpler, let's pick a random point A as an example.

Given point A, we need to calculate all slopes between A and other points. There will be three cases:

Some other point is the same as point A.

Some other point has the same x coordinate as point A, which will result to a positive infinite slope.

General case. We can calculate slope.

We can store all slopes in a hash table. And we find which slope shows up mostly. Then add the number of same points to it. Then we know the maximum number of points on the same line for point A.

We can do the same thing to point B, point C...

Finally, just return the maximum result among point A, point B, point C...
"""
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict
class Solution(object):
	def maxPoints(self, points):
		res = 0
		for i in range(len(points)):
			samePoint = 1
			d = defaultdict(int)
			for j in range(i+1,len(points)):
				if points[i].x == points[j].x and points[i].y == points[j].y:
					samePoint +=1
				elif points[i].x == points[j].x :
					d[sys.maxint] +=1
				else:
					slope = float(points[i].y - points[j].y)/float(points[i].x - points[j].x) #这里python的精确度不够。。反正不能用int
					d[slope] +=1
		
			localMax = 0
			for k in d.keys():
				localMax = max(localMax,d[k])
			localMax += samePoint
			res = max(localMax,res)
		
		return res			

                
        
        				
