class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode('utf-8'))
        x = int(h.hexdigest(),16)

        put_to = x%5
        # print(x%5)
        node = ListNode(x)
        if self.data[put_to]:
            cur = self.data[put_to]
            while cur:
                if cur.next != None:
                    cur = cur.next
                else:
                    cur.next = node
                    return
        else:
            
            self.data[put_to] = node
            return 


    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        if self.find(key) == None:
            return 
        else:
            while self.find(key) != None:
                if self.find(key).next != None:
                    cur = self.find(key)
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                    
                else:
                    cur = self.find(key)
                    cur.val = None
                    
            return
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        if self.find(key) == None:
            print(False)
            return False
        else:
            print(True)
            return True


    def find(self, target):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(target.encode('utf-8'))
        target = int(h.hexdigest(),16)

        

        for i in range(0,self.capacity):
            root = self.data[i]
            if root:
                cur = root
                while cur:
                    if cur.val == target:
                        print(cur.val)
                        return cur
                    elif cur.next != None:
                        cur = cur.next
                    elif cur.next == None:
                        break
            else:
                pass
        print(None)
        return None

"""  
## Ref.
[wiki-雜湊函式](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8)

[wiki-MD5](https://zh.wikipedia.org/wiki/MD5)

[8. Hashing with Chaining](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)

[1 分鐘搞懂 Python 迴圈控制：break、continue、pass](https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8)

[Shallow vs Deep Copying of Python Objects](https://realpython.com/copying-python-objects/#copying-arbitrary-python-objects)

"""