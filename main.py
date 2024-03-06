class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    
    def print(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next
        print('null')


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.print()