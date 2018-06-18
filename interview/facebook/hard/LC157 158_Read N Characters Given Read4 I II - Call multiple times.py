"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
"""
用一个临时数组，存放每次read4读到字符，再用一个指针标记buf数组目前存储到的位置，然后将这个临时数组的内容存到buf相应的位置就行了。
这里需要注意两个corner case：
1.如果本次读到多个字符，但是我们只需要其中一部分就能完成读取任务时，我们要拷贝的长度是本次读到的个数和剩余所需个数中较小的
2.如果read4没有读满4个，说明数据已经读完，这时候对于读到的数据长度，因为也可能存在我们只需要其中一部分的情况，所以要返回总
所需长度和目前已经读到的长度的较小的

"""
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        temp = ["","","",""]
        m = -1
        # 达到需求 m ==0, 文本没了 m < 4
        while m != 0:
            m = read4(temp)
            m = min(n - total, m)
            for i in range(m):
                buf[total] = temp[i]
                total += 1
        return total


#!/usr/bin/python

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""
# The read4 API is alreadsy defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
"""
又是一开始没看懂题。变化是这样：比如先call了n=3，然后call n=5，那么第一次就读入了4个char，第二次call应该把上一次的最后一个char拿来。也就是说要有个cache取
缓存已读取的字符，然后从这个cache里面取。

每次读4个字符，放入 cache，然后

in = Math.min(n - total, buff.size()) 这个是精髓，这样就知道还需要多少个字符了。如果是in=0了，那么说明已经够了或者没字符了，这样就不用再读取了。否则无论哪个大，
接下来都需要往buf中放入in个字符（可能是剩的少，也有可能要求的少）。
"""
# 优化是用传进去的buffer做temporary buf 

# 链接: https://instant.1point3acres.com/thread/271245

class Solution(object):
    def __init__(self):
        self.buff = deque()
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        temp = ["","","",""]
        m = -1
        while m != 0:
            m = read4(temp)
            for i in range(m):
                self.buff.append(temp[i])
            m = min(n - total, len(self.buff))
            for i in range(m):
                buf[total] = self.buff.popleft()
                total += 1
        return total

#利扣 妖舞扒变形，给了read4，但是实现按行read，会有'/n'为行终止，这题开始没理清题意，以为总是以行终止作为结束，就没考虑读完的情况，
# 后来面试官提醒说不一定最后是行终止字符才发现少了个if，悲剧， 大家一定要问清题意再作答啊 
class Solution(object):
    def __init__(self):
        self.buff = deque()
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        temp = ["","","",""]
        m = -1
        while m != 0:
            m = read4(temp)
            for i in range(m):
                self.buff.append(temp[i])
            m = min(n - total, len(self.buff))
            for i in range(m):
                buf[total] = self.buff.popleft()
                total += 1
                if buf[-1] == '\n':
                    return total
        return total

        