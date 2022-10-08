#Program to implement Deque

'''
Deque is a double ended queue. It can be used to add or remove elements from either front or rear.
'''

import collections


class Deque:
    def __init__(self):
        self.queue = collections.deque()
    
    def addFront(self, data):
        self.queue.appendleft(data)
    
    def addBack(self, data):
        self.queue.append(data)
    
    def removeFront(self):
        self.queue.popleft()

    def removeBack(self):
        self.queue.pop()
    
    def printQueue(self):
        print("Elements in the queue:")
        print(self.queue)

obj = Deque()
obj.addFront(14)
obj.addFront(22)
obj.addBack(13)
obj.addBack(-6)
obj.printQueue()
obj.removeFront()
print("Elements after removing front element:")
obj.printQueue()
obj.removeBack()
print("Elements after removing back element:")
obj.printQueue()