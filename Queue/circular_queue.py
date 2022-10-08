#Circular Queue Implementation in Python

'''
Circular Queue is an extended version of Queue where the last position is connected back to the first position to make a circle.
It is also called ‘Ring Buffer’.
'''

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    
    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        #if elements are present in the queue
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.front == self.rear):
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def printQueue(self):
        i = self.front

        if (self.front == -1 and self.rear == -1):
            print("Queue is Empty")
        
        else:
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[self.rear], end=" ")
            print()

obj = CircularQueue(5)
obj.enqueue(14)
obj.enqueue(22)
obj.enqueue(13)
obj.enqueue(-6)
obj.printQueue()
print("Deleted value = ", obj.dequeue())
print("Deleted value = ", obj.dequeue())
obj.printQueue()
obj.enqueue(9)
obj.enqueue(20)
obj.enqueue(5)
obj.printQueue()
