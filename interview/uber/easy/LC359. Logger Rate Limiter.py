class Logger(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.d = dict()
		

	def shouldPrintMessage(self, timestamp, message):
		"""
		Returns true if the message should be printed in the given timestamp, otherwise returns false.
		If this method returns false, the message will not be printed.
		The timestamp is in seconds granularity.
		:type timestamp: int
		:type message: str
		:rtype: bool
		"""
		if message in self.d:
			if timestamp - self.d[message] < 10:
				return False
			
		self.d[message] = timestamp
		return True
			
# Your Logger object will be instantiated and called as such:
obj = Logger()
print obj.shouldPrintMessage(1, "foo")
print obj.shouldPrintMessage(2,"bar")
print obj.shouldPrintMessage(3,"foo")
print obj.shouldPrintMessage(8,"bar")
print obj.shouldPrintMessage(10,"foo")
print obj.shouldPrintMessage(11,"foo")

因为rate limiter是先进先出，所以用q，pop掉旧的记录，然后剩下都是合格的，数一下合格的有没有超过10个，
如果没有就加进去，不然就reject