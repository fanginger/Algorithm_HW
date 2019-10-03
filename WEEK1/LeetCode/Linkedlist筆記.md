# Linkedlist 演算法筆記


## linkedlist 每個object所長的樣子
![](https://i.imgur.com/RweO6sZ.png)
### 每個object都會有
- data
- next(pointer會指向的)
    - self.head = node，是指向整個node並不是只像那個node的data
    
## ok,那我們來初始化
想要建立的class
- Node
    - data
    - next
    - last
        - 可以指出上一個是誰(在練習已經加入)
- LinkedList
    - head
        - 指出現在頭部是誰
    - tail
        - 指出現在尾部是誰(在練習已經加入)
    - len
        - 說出現在長度，在各方面很好使用

## 新增刪除取值

新增：addAtHead、addAtTail、addAtIndex
刪除：deleteAtIndex
取值：get

### addAtHead
ok，先來想想接入頭部要如何去加入呢？
>一定是把self.head的pointer指向加入項吧？
然後再把加入像的pointer指向原本的

ok示意圖大概長這樣(bty我用aww畫的，希望有平板讓我畫得更好)
![](https://i.imgur.com/fYVr0q2.png)

然後條件式分為
- self.head原本後面就是None
- 後面有東西

```python=
def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            #這裡是指出原本在head指向的node
            self.head = node
            node.next = tmp

```
### addAtTail


>attail我的想法是找出最尾端的再把要新增的加進去
>
![](https://i.imgur.com/thJRQed.png)

條件式分為
- self.head後面是空的
- 後面不是空的，就得找出最尾端

```python=
 def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        else:
            curr = self.head
            while curr:
                if curr.next != None:
                #如果curr.next下一個是空的就代表現在已經是最尾巴
                    curr = curr.next
                else:
                #現在的curr已經是最尾巴所以把next指向現在要加入的node return!!
                    curr.next = node
                    return

```


### addAtIndex

>找出現在index-1的node將他的next加入新的node，再把新的node的next指向原本接的

![](https://i.imgur.com/VAdgWmi.png)


條件式分為
- index為負，加入到最前
- index為正值，找出curr等於index-1的
    - 找出事不是大於len

```python=
def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        curr = self.head
        index -=1
        if index<0:
                self.addAtHead(node)
        else:
            if curr ==None:
                return     
            else:
                 for i in range(0,index):
                    # curr = curr.next
                    if curr == None:
                        return
                    else:
                        curr = curr.next
            tmp = curr.next
            curr.next = node
            node.next = tmp

```

## deleteAtIndex
![](https://i.imgur.com/C2OA8o0.png)

條件式分為
- index為負，直接回
- index為正
    - index ==0就改掉self.head接的頭
    - 慢慢找到curr==index-1的node再來跳過那個值
```python=
def deleteAtIndex(self, index: int) -> None:
        if index<0:
            return
        else:
            curr = self.head
            len = 0
            if index == 0:
                self.head =self.head.next
            else:
                while curr:
                    if index-1 == len:
                        if curr.next == None:
                            return
                        else:
                            curr.next=curr.next.next
                            return 
                    else:
                        curr = curr.next
                        len += 1

```


### get

條件式分為
- index為負，直接回-1
- index為正
    - 慢慢找出index == len的值
    - 超過長度回-1
```python=
 def get(self, index: int) -> int:
        if index < 0 :
            return -1
        else:
            curr = self.head
            len = 0
            while curr:
                if index == len:
                    return curr.val
                else:
                    curr = curr.next
                    len += 1
            return -1 


```