"""
给你一个timestamp和collection of 投票, 找当时timestamp得票最高的参选者
"""
from collections import OrderedDict
from collections import defaultdict
import copy
class Vote(object):
    def __init__(self):
        self.m = OrderedDict()
        self.curm = defaultdict(int)
    
    def vote(self, timestamp, votes):
        for k, v in votes.items():
            self.curm[k] += v
        self.m[timestamp] = copy.deepcopy(self.curm)         
    def get(self, timestamp):
        mm = {}
        for t, v in self.m.items():
            if t > timestamp:
                break
            mm = v
        kk, vv = "#", 0     
        for k, v in mm.items():
            if v > vv:
                kk, vv = k, v
        return k
        
v = Vote()        
v.vote("12:30", {"a":3, "b":2})
v.vote("13:30", {"a":2, "b":1})
v.vote("14:30", {"a":5, "b":4})
print(v.get("14:00"))
