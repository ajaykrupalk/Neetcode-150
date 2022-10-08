#Program to implement a queue

'''
Queue is a linear data structure which follows the order of First In First Out (FIFO). 
'''

import collections

def create_queue():
    queue = collections.deque()
    return queue

def check_empty(queue):
    return len(queue)==0

def enqueue(queue, item):
    queue.append(item)
    print('Enqueued Item: '+str(item))

def dequeue(queue):
    if check_empty(queue):
        return "Stack is empty"
    return queue.popleft()

queue = create_queue()
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
print("Element Dequeued is:",dequeue(queue))
print("Elements after Dequeue Operation is",queue)