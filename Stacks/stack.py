#Program to implement a stack

'''
A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
'''

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Pushed item: " + str(item))

def pop(stack):
    if check_empty(stack):
        return 'Stack is empty'

    return stack.pop()

stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
print("Popped Item: " + str(pop(stack)))
print("Stack after popping an element: " + str(stack))