# 面经出现： +1
"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

class Solution:
    def addOperators(self, nums, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def dfs(start, expr, val, off):
            if start == len(nums):
                if val == target:
                    res.append(expr)
            else:
                for i in range(start, len(nums)):
                    if nums[start] == "0" and i != start:
                        continue
                    num = int(nums[start: i + 1])
                    if start == 0:
                        dfs(i + 1, nums[start: i + 1], num, num)
                    else:
                        dfs(i + 1, expr + "+" + nums[start: i + 1], val + num, num)
                        dfs(i + 1, expr + "-" + nums[start: i + 1], val - num, -num)
                        dfs(i + 1, expr + "*" + nums[start: i + 1], val - off + off * num, off * num)
        dfs(0, "", 0, 0)
        return res


        
class Solution(object):
	"""
	https://segmentfault.com/a/1190000003797204
	因为要输出所有可能的情况，必定是用深度优先搜索。问题在于如何将问题拆分成多次搜索。加减法很好处理，每当我们截出一段数字时，将之前计算的结果加上或者减去这个数，就可以将剩余的数字字符串和新的计算结果代入下一次搜索中了，直到我们的计算结果和目标一样，就完成了一次搜索。
	然而，乘法如何处理呢？这里我们需要用一个变量记录乘法当前累乘的值，直到累乘完了，遇到下一个加号或减号再将其算入计算结果中。这里有两种情况:

	乘号之前是加号或减号，例如2+3*4，我们在2那里算出来的结果，到3的时候会加上3，计算结果变为5。在到4的时候，因为4之前我们选择的是乘号，这里3就应该和4相乘，而不是和2相加，所以在计算结果时，要将5先减去刚才加的3得到2，然后再加上3乘以4，得到2+12=14，这样14就是到4为止时的计算结果。
	另外一种情况是乘号之前也是乘号，如果2+3*4*5，这里我们到4为止计算的结果是14了，然后我们到5的时候又是乘号，这时候我们要把刚才加的3*4给去掉，然后再加上3*4*5，也就是14-3*4+3*4*5=62。这样5的计算结果就是62。
	因为要解决上述几种情况，我们需要这么几个变量，一个是记录上次的计算结果pre，一个是记录上次被加或者被减的数val，一个是当前准备处理的数cur。当下一轮搜索是加减法时，val就是简单换成cur，当下一轮搜索是乘法时，val是val乘以cur。
	"""
	def addOperators(self, num, target):
		res = []
		self.helper(res, "", num, target, 0, 0, 0)
		return res
	
	def helper(self,res, path, num, target, pos, pre, val):
		if pos == len(num):
		    if target == int(pre):
		        res.append(path)
			return
		
		for i in range(pos,len(num)):
			if i != pos and num[pos] == '0':#我们截出的数字不能包含0001这种前面有0的数字，但是一个0是可以的。这里一旦截出的数字前导为0，就可以return了，因为说明前面就截的不对，从这之后都是开始为0的，后面也不可能了。
				break
			cur = int(num[pos:i+1])
			if pos == 0:
			    self.helper(res,path+str(cur), num, target,i+1,cur,cur)
			else:
				self.helper(res,path+"+"+str(cur), num, target,i+1,pre+cur,cur)
				self.helper(res,path+"-"+str(cur), num, target,i+1,pre-cur,-cur)
				self.helper(res,path+"*"+str(cur), num, target,i+1,pre-val+val*cur,val*cur)


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        """
        pre: expression s -> value
        val: pre - pre', the adding value to pre
        if "*", offset previous val and add new val * cur
        """
        def walk(idx, pre, val, s):
            if idx == len(num):
                if pre == target:
                    res.append(s)
            else:
                for i in range(idx, len(num)):
                    #"01"
                    if num[idx] == "0" and i != idx:
                        break
                    cur = int(num[idx: i + 1])
                    if idx == 0:
                        #"only *"
                        walk(i + 1, cur, cur, str(cur))
                    else:
                        #"+", "-", "*"
                        walk(i + 1, pre + cur, cur, s + "+" + str(cur))
                        walk(i + 1, pre - cur, - cur, s + "-" + str(cur))
                        walk(i + 1, pre - val + val * cur, val * cur, s + "*" + str(cur))
        walk(0, 0, 0, "")
        return res