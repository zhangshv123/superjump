"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate
the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2  capacity  );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

"""
The problem can be solved with a hashtable that keeps track of the keys and its values in the double linked list. 
One interesting property about double linked list is that the node can remove itself without other reference. 
In addition, it takes constant time to add and remove nodes from the head or tail.

One particularity about the double linked list that I implemented is that I create a pseudo head and tail to 
mark the boundary, so that we don't need to check the NULL node during the update. This makes the code more concise 
and clean, and also it is good for the performance as well.
"""

"""
lazy版本：
直接用linkedin hash map
This is the laziest implementation using Java's LinkedHashMap. In the real interview, however, it is definitely not what interviewer expected.
"""
from collections import defaultdict
class Node:
    def __init(self):
        self.prev = None
        self.next = None
        self.val = -1
        self.key = -1

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Remove an existing node from the linked list.             
    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    # Always add the new node right after head 
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)    
        
    def popTail(self):
        res = self.tail.prev
        self.removeNode(res)
        return res
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if node == None:
            return -1
        self.moveToHead(node)
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key, None)
        if node == None:
            node = Node()
            node.key, node.val = key, value
            self.cache[key] = node
            self.addNode(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.popTail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.moveToHead(node)