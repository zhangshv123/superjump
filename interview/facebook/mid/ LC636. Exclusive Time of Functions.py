"""
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts 
from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions 
should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
"""
"""
In a more conventional approach, let's look between adjacent events, with duration time - prev_time. 
If we started a function, and we have a function in the background, then it was running during this time. 
Otherwise, we ended the function that is most recent in our stack.

stack只存function的id
栈中保存元素格式为函数ID，时间戳 [fid, tmp]

当日志为'start'时：

    若栈非空，记栈顶元素为topFid, topTmp；将fid的时间累加tmp - topTmp；

    将[fid, tmp]压栈

否则：

    将栈顶元素的时间累加tmp - topTmp + 1

    弹出栈顶元素

    若栈非空，将栈顶元素topTmp更新为tmp + 1
"""
def exclusiveTime(self, N, logs):
	ans = [0] * N
	stack = []
	prev_time = 0

	for log in logs:
		fn, typ, time = log.split(':')
		fn, time = int(fn), int(time)

		if typ == 'start':
			if stack:
				ans[stack[-1]] += time - prev_time 
			stack.append(fn)
			prev_time = time
		else:
			ans[stack.pop()] += time - prev_time + 1
			prev_time = time + 1

	return ans
