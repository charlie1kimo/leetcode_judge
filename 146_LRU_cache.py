"""
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item. 
"""
class LRUCache(object):
    """
    Idea:
        - use dict() (HashMap) for keys store; (key = key, val = node) (O(1), use search then O(n)!)
        - use DoublyLinkedList for data store O(1)

    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = dict()
        self.data = DoublyLinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.data.moveToTail(node)
        return node.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.keys:
            node = self.keys[key]
            self.data.moveToTail(node)
            node.val = value
        else:
            node = DoublyLinkedListNode(key, value)
            self.keys[key] = node
            self.data.insertTail(node)
            if len(self.keys) > self.capacity:
                # remove head
                head = self.data.head
                self.data.delete(head)
                del self.keys[head.key]


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        self.size -= 1

    def insertTail(self, node):
        self.size += 1
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def moveToTail(self, node):
        if self.tail == node:
            return
        self.delete(node)
        self.insertTail(node)

    def __repr__(self):
        s = ""
        curr = self.head
        while curr != None:
            s += "%s -> " % repr(curr)
            curr = curr.next

        return s

class DoublyLinkedListNode(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<DoublyLinkedListNode(%d, %d)>" % (self.key, self.val)
