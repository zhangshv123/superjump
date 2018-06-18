#!/usr/bin/python
"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
"""
insert()：对于插入操作，我们遍历字符串同时，根据上一个节点的哈希表来找到下一个节点，直到哈希表中没有相应的字母，
我们就新建一个节点。然后从这个新建节点开始，用同样的方法把剩余的字母添加完。记住最后一个字母要添加叶子节点的标记，
表明这个词到此已经完整了。
search()：对于搜索操作，我们也是遍历字符串，然后根据每个节点的哈希表找到路径，最后返回该字符串最后一个字母所在节点。
如果中途有找不到路径的情况就直接返回null，如果找到了最后的节点，如果它也是叶子结点的话，就说明找到了。
startWith()：使用和search()，一样的方法，只是我们返回的节点不用判断是否是叶子节点。只要找到就行。

"""
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)