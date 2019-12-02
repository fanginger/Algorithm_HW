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
        h = MD5.new()
        h.update(key.encode('utf-8'))
        x = int(h.hexdigest(),16)
        # 轉換為10進位
        put_to = x%5
        # print(x%5)
        node = ListNode(key)
        if self.data[put_to]:
            #先找有沒有存在
            # 開始找最尾巴
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
            if self.find(key).next != None:
                cur = cur.next 
                return 
            else:
                cur = self.find(key)
                cur.val = None
                # self.find(key).val = None
                return
            # cur = self.find(key)
            # cur = cur.next 
            # return 
            # for i in range(0,self.capacity):
            #     root = self.data[i]
            #     if root:
            #         cur = root
            #         while cur:
            #             if cur.val == key:
            #                 cur = cur.next
            #                 return cur
            #             elif cur.next != None:
            #                 cur = cur.next
            #             elif cur.next == None:
            #                 break
            #         else:
            #             pass
                
            #     return None
        
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

    
from Crypto.Hash import MD5
myhash = MyHashSet()
myhash.add('dog')
myhash.add('pig')
# myhash.add('pi')
# myhash.add('pg')
# myhash.add('pgig')
# myhash.add('psig')
# myhash.add('pisg')
# myhash.add('piag')
# myhash.add('piaag')
# myhash.add('piaaag')
rel = myhash.contains('pig')
print(rel)
rel = myhash.contains('dog')
print(rel)
rel = myhash.contains('cat')
print(rel)
myhash.add('bird')
rel = myhash.contains('bird')
print(rel)
rel = myhash.remove('pig')
rel = myhash.contains('pig')
print(rel)