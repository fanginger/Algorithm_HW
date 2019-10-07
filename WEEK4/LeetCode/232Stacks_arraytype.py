class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
       
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)
        for i in range(len(self.a)-1,0,-1):
            self.a[i] = self.a[i-1]
        self.a[0] = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        c = self.a.pop()
        print(c)
        return c
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        length = len(self.a)-1
        return self.a[length]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.a) == 0:
            print('true')
            return True
        else:
            for i in range(len(self.a)):
                if self.a[i] != None:
                    print('false')
                    return False
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()