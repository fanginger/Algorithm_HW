class Node:
    def __init__ (self,data,next =None):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        
    def print(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        node = Node(x)
        #區分看裡面有沒有值
        if(self.head == None):
            self.head = node
            self.tail=node
            
        else:
            #裡面有值，所以說要加進頭部
            tmp = self.head
            self.head = node
            node.next = tmp
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
      
        if(self.head==None):
            return None
        else:
            cur = self.head
            tmp = self.tail
            if cur != None:
                
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return cur.data
                else:
                    #現在要找出最後一個和最後一個的前一個
                    while cur.next != self.tail:
                        cur = cur.next
                    #找出最後的前一個     
                    cur.next = None
                    self.tail = cur
                    return tmp.data
            
    def peek(self) -> int:
        """
        Get the front element.
        """
        if(self.head == None):
            return None
        else:
            return self.tail

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(self.head == None):
            return True
        else:
            return False
        

