Problem:
	Factor Combinations

	Numbers can be regarded as product of its factors. For example,

	8 = 2 x 2 x 2;
		= 2 x 4.
	Write a function that takes an integer n and return all possible combinations of its factors.

	e.g.,
	input: 12
	output:
	[
		[2, 6],
		[2, 2, 3],
		[3, 4]
	]  
	--------------
	def factor(n):
			res = []
			self.helper(2,n,path,res)
			return res

	/**计算机里面有CPU和MEMORY,其他不是必须的，然后memory里面有stack和heap，stack也是先进先出，向下，heap是向上
	 * stack(有限的) && heap（无限的）
	recursive的优点:readable,代码短，快
	non-recursive:不会stack Overflow ,晦涩，不好写
	空间时间都是一样的！
	 */
	def helper(start,n,path,res):
		 if len(path) > 0:
				 res.append(path+[n])
			for i in range(start,int(math.sqrt(n))+1):
					if n%i == 0:
							path.append(i)
							self.helper(i,n/i,path,res)
							path.pop()

	def nonrecursive(n, res):
			path = []
			start = 2
			while (True):
					# find the first qualified factor
					target = -1
					for i in range(start, int(sqrt(n)) + 1):
							if n % i == 0:
									target = i
									break
					if target != -1: # found a qualified factor target
							# push
							path.append(target)
							# update
							start = target
							n = n / target
					else: # failed to find
							if len(path) == 0: # while-loop end condition
									break
							res.append(path + [n])
							# pop
							top = path.pop()
							# back-tracking
							start = top + 1
							n = n * top
				 
							
							
							
					
					
			

				 
							
