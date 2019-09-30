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

## 新增刪除
新增：addAtHead、addAtTail、addAtIndex
刪除：deleteAtIndex

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

![](https://i.imgur.com/thJRQed.png)


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
                    curr = curr.next
                else:
                    curr.next = node
                    return

```