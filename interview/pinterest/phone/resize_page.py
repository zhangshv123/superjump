import heapq
class pin:
	def __init__(self, id = 0, height = 0):
		self.id = id
		self.height = height
		
	
	def arrage(self, pins, col):
		h = []
		res = []
		for i in range(len(pins)):
			if i < col:
				res.append([pins[i].id])
				heapq.heappush(h, (pins[i].height,i))
			else:
				cur = heapq.heappop(h)
				heapq.heappush(h, (cur[0]+pins[i].height, cur[1]))
				res[cur[1]].append(pins[i].id)
		return res

s = pin()
pins = []
pin1 = pin(1,100)
pin2 = pin(2,200)
pin3 = pin(3,150)
pins.append(pin1)
pins.append(pin2)
pins.append(pin3)
print s.arrage(pins,2)
	
			
		
		
		
	