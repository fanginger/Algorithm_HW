class Node:
    def __init__(self, data, next=None, last=None):
        self.data = data
        self.next = next
        self.last = last
    def __repr__(self):
        return str(self.data)

class LinkList:
    def __init__(self, maxLen):
        self.head = None   
        self.right = None 
        self.len = 0
        self.maxLen = maxLen

    def print(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    # def addTail(self, node):
    #     if self.head == None:
    #         self.head = node
    #         self.right = node
    #         self.len += 1
    #     else:
    #          curr = self.head
    #          while curr:
    #              if curr.next != None:
    #                 curr = curr.next # jump jump jump
    #              else:   
    #                 curr.next = node # add
    #                 self.len += 1
    #                 self.right = cur.next

    #                 return

    def enqueue(self, node):
        if self.len < self.maxLen:
            if self.head == None:
                self.head = node
                self.right = node
                self.len += 1
            else:
                curr = self.head
                self.head = node
                self.head.next = curr
                self.len += 1


    # def addAtIndex(self, index, node):
    #     if index < 0:
    #         self.addHead(node)
    #     else:
    #         count = 0
    #         cur = self.head
    #         for i in range(index):
    #             cur = cur.next
    #             if cur == None:
    #                 print('out of index')
    #                 return  
    #         tmp = cur.next
    #         cur.next = node
    #         node.next = tmp
    
    # def deleteAtIndex(self, index):
    #     if index < 0:
    #         print('out of index')
    #         return
    #     elif index == 0:
    #         self.head = self.head.next
    #         pass
    #     else:
    #         count = 0
    #         cur = self.head
    #         for i in range(index-1):
    #             cur = cur.next
    #         if cur.next == None:
    #             print('out of index')
    #             return  
    #         cur.next = cur.next.next
            

            




linklist1 = LinkList(3) 
linklist1.enqueue(Node(1))
linklist1.enqueue(Node(2))
linklist1.enqueue(Node(3))
# linklist1.addTail(Node(6))
# linklist1.deleteAtIndex(2)
# linklist1.addHead(Node(4))
# linklist1.addAtIndex(3, Node(9))
linklist1.print()
