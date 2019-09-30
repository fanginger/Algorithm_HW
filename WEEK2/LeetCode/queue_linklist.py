class Node:
    def __init__(self, data, next=None, last=None):
        self.data = data
        self.next = next
        self.last = last
    def __repr__(self):
        return str(self.data)

class Queue:
    def __init__(self, maxLen):
        self.head = None   
        self.right = None 
        self.len = 0
        self.maxLen = maxLen

    def printFromLeft(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    def printFromRight(self):
        curr = self.right
        while curr:
            print(curr)
            curr = curr.last        

    def enqueue(self, node):
        if self.head == None:
            if self.len < self.maxLen:
                self.head = node
                self.right = node
                self.len += 1
        else:
            curr = self.head
            self.head = node
            self.head.next = curr
            curr.last = node
            self.len += 1
            if self.len > self.maxLen: # Ensure list length is within maxLen
                self.right = self.right.last
                self.len -= 1
    def dequeue(self):
        if self.len > 0:
            tmp = self.right
            self.right = self.right.last
            self.len -= 1
            return tmp
        else:
            return 'I have nothing to dequque'

            
queue1 = Queue(3) 
# queue1.enqueue(Node(1))
# queue1.enqueue(Node(2))
# queue1.enqueue(Node(3))
# queue1.printFromRight()
print(queue1.len)
print(queue1.dequeue())
print(queue1.len)
