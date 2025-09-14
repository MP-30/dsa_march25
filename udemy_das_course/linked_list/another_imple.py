class Node:
     def __init__(self, data):
          self.data = data
          self.next = None
          
a = Node(3)
b = Node(5)
c = Node(8)

head = a
head.next = b
b.next = c

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# traverse linked list
def printLinkedList():
    curr = head 

    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next
        
printLinkedList()

# insertion in linked list

