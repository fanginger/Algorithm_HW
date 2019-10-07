class Node:
    def __init__(self, data, next=None, last=None):
        self.data = data
        self.next = next
        self.last = last
    def __repr__(self):
        return str(self.data)

class Stack:
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

    def push(self, node):
        if self.len < self.maxLen:
            if self.head == None:
                    self.head = node
                    self.right = node
                    self.len += 1
            else:
                    curr = self.head
                    self.head = node
                    self.head.next = curr
                    curr.last = node
                    self.len += 1

    def pop(self):
        if self.len > 0:
            tmp = self.head
            self.head = self.head.next
            self.len -= 1
            return tmp
        else:
            return 'I have nothing to pop'

            
stack1 = Stack(3) 
stack1.push(Node(1))
stack1.push(Node(2))
stack1.push(Node(3))
stack1.push(Node(4))

# stack1.printFromRight()

print('my len = ', stack1.len)
print(stack1.pop())
print('my len = ', stack1.len)
