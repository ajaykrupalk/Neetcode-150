#Python program to reverse a linked list

def reverseList(self, head):
    prev, curr = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev