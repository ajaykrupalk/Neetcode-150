#Program to implement Priority queue

'''
Priority Queue is a special type of queue in which each element is associated with a priority and is served according to its priority.
'''

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def addElements(self, data):
        self.queue.append(data)
    
    def removeElements(self):
        try:
            maxVal = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxVal]:
                    maxVal = i
            item = self.queue[maxVal]
            del self.queue[maxVal]
            return item
        except IndexError:
            print()
            exit()

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    obj = PriorityQueue()
    obj.addElements(12)
    obj.addElements(1)
    obj.addElements(14)
    obj.addElements(7)
    print("Elements in the queue:")
    obj.printQueue()
    print("Removed element:", obj.removeElements())