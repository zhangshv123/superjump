题目：
一个string和一个wordlist
例子：
“tihssiasmple” 和word list["this", "is", "a","sample"]
返回true和false
from collections import defaultdict
def ismorphicString(str, wordList):
	d = makeDict(wordList)
	return dfs(str, d, 0)
	
def dfs(str, d, start):
	if start == len(str):
		return True
	for i in range(start, len(str)):
		sortedWord = ''.join(sorted(str[start:i+1]))
		if sortedWord in d:
			 if dfs(str, d, i+1):
				return True
	return False
			

def makeDict(wordList):
	d = defaultdict(list)
	for word in wordList:
		d[''.join(sorted(word))].append(word)
	return d
	
print ismorphicString("thissisaassample", ["this", "is", "a", "sample"])
	