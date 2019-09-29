class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data)

class LinkList:
    def __init__(self):
        self.head = None        
    def print(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    def addTail(self, node):
        if self.head == None:
            self.head = node
            return
        else:
             curr = self.head
             while curr:
                 if curr.next != None:
                    curr = curr.next
                 else:   
                    curr.next = node



linklist1 = LinkList() 
linklist1.addTail(Node(3))
linklist1.addTail(Node(6))
linklist1.print()