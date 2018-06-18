from collections import defaultdict
class Solution(object):
	def minWindow(self, s, t):
		freqT = defaultdict(int)
		freqS = defaultdict(int)
		
		for char in t:
			freqT[char] +=1
		
		found = 0
		start = 0
		result = ""
		
		for i in range(len(s)):
			if s[i] in freqT:
				freqS[s[i]] +=1
				if freqS[s[i]] <= freqT[s[i]]:
					found += 1
				
                # if solution exists
				if found == len(t):
                    #delete till minimum requirement is meet
					while s[start] not in freqT or freqS[s[start]] > freqT[s[start]]:
						if s[start] in freqT:
							freqS[s[start]] -=1
						start += 1
                    #update result
					if result == "" or i - start +1 < len(result):
						result = s[start:i+1]
		return result
        