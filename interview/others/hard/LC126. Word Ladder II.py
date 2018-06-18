"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
"""
而对于这道加强版来说，还需要输出所有符合最短长度的变换的路径，这道题的时间要求非常BT。。所以基本的解题思想是“

1、首先和127的方式一样，使用BFS遍历，不过这次的主要目的是记录出每个单词的最短变换长度（高度）,即从start开始变换多少步可以到达 
2、使用dfs的方式，从endword开始，根据1得到的高度按照深度优先的方式进行路径查找，当找到startword后加入一条路径（注意dfs方法里
的beginword endword和原题的相反，答案也要做翻转）


"""

from string import ascii_lowercase
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        visited = defaultdict(set)
        q = [beginWord]
        wordList = set(wordList)
        level = 1
        while len(q) > 0:
            newQ = []
            if endWord in q:
                break
            level_map = defaultdict(set)                
            for cur in q:
                for i in range(len(cur)):
                    for c in ascii_lowercase: 
                        newW = cur[:i] + c + cur[i + 1:]  
                        if newW == cur:
                            continue
                        if newW not in wordList or newW in visited:
                            continue
                        if newW not in level_map:
                            newQ.append(newW)
                        level_map[newW].add(cur)
            visited.update(level_map)
            q = newQ
        paths = []     
        def dfs(word, path):
            if word == beginWord:
                paths.append(path[::-1])
            else:
                for parent in visited[word]:
                    path.append(parent)
                    dfs(parent, path)
                    path.pop()
        dfs(endWord, [endWord])
        return paths





from collections import deque
from string import ascii_lowercase
import sets
class Node(object):
    def __init__(self, word):
        self.word = word
        self.parents = []
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        wordList = set(wordList)
        q, visitedMap, level = [], {}, 0
        q.append(beginWord)
        visitedMap[beginWord] = Node(beginWord)
        while len(q) > 0 :
            size = len(q)
            level += 1
            # print level, map(lambda a: a.word, q)
            if endWord in q:
                break
            new_q = []
            for word in q:
                node = visitedMap[word] 
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        #same word
                        if c == word[i]:
                            continue
                        newWord = word[:i] + c + word[i+1:]
                        if newWord not in wordList:
                            continue    
                        if newWord not in visitedMap:
                            visitedMap[newWord] = Node(newWord)
                            new_q.append(newWord)
                        if newWord in new_q:
                            visitedMap[newWord].parents.append(node)
            q = new_q
        if endWord not in visitedMap:
            return []
        stk, array, res = [], ["" for _ in range(level)], []
        stk.append((visitedMap[endWord], 0))
        # print level, map(lambda word: (word, map(lambda a: a.word, visitedMap[word].parents)), visitedMap.keys())
        while len(stk) > 0:
            node, height = stk.pop()
            # print node.word, height, map(lambda a: a.word, node.parents)
            array[height] = node.word
            if height == level - 1 and node.word == beginWord:
                res.append(array[::-1])
            for parent in node.parents:
                stk.append((parent, height + 1))
        return res
            
            
import sets
from collections import deque
from string import ascii_lowercase
class DAGNode(object):
    def __init__(self, word):
        self.word = word
        self.parents = []

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        s, m, q = set(), {}, deque()
        m[beginWord] = DAGNode(beginWord)
        q.append(m[beginWord])
        while len(q) > 0:
            m = {}
            size = len(q)
            for i in range(size):
                node = q.popleft()
                word = node.word
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word not in wordSet:
                            continue
                        if new_word in s:
                            continue
                        if new_word not in m: 
                            m[new_word] = DAGNode(new_word)
                            q.append(m[new_word])
                        m[new_word].parents.append(node)
            for word, node in m.items():
                s.add(word)
            if endWord in m:
                break
        path, res = [], []
        def walk(node):
            path.append(node.word)
            if node.word == beginWord:
                res.append(path[::-1])
            for pNode in node.parents:
                walk(pNode)
            path.pop()
        if endWord in m:
            walk(m[endWord])
        return res
                        
                
                        
            
            
                
            
            
                
            
            
                