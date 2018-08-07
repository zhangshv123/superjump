#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT

# rate limiter

# ---------------------------> t
#   x     x     ?    x     xxxxx|||


# client-side rate limiter

counter = deque()
index: time(map from time to integer)
value: number of calls
dict: map from counter array index to exat time
0000 = 0
0001 = 1
0002 = 2

counter[1] = 1000


1000 = 1000

def _call_external_api():
	# already implemented
	# sends a http get request to some external api (or similar)
	pass

	
	

def call_external_api_rate_limited(time):
	# wrapper function around _call_external_api
	# that implements rate limiting
	# rate limit: 10 external calls per second
	# if rate limit exceeded, reject and raise an exception
	# otherwise, allow the external call
	now = get_current_time_ms()
	
	while now - counter[0] > 1000:
		counter.popleft()
	if len(counter) < 9:
		_call_external_api()
		counter.append(now)
	else:
		print "too many call here!"  
		
	
	
	
	
	
	
	
	global counter
	now = get_current_time_ms()
	start = now - 1000
	diff = counter[now] - counter[start]
	 if diff< 10:
			_call_external_api()
			counter[now] += 1
		else:
			print "too many call here!"
	
	return counter
	
def get_current_time_ms():
	# returns current time in milliseconds (since Jan 1, 1970)
	