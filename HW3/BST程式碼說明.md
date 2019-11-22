# Binaray Search Tree
分為主要
- insert 
- delelte
- search
- modify 
- print


## 新增
簡單來說就是找到要放進點的位置然後加入
簡單流程圖大概是這樣
![](https://i.imgur.com/NR80m6j.png)

前面都會加入clean function

全部程式碼解釋
```python
def insert(self, root, val):
        
        self.clean(root)
        # 因為不確定樹是不是正確的，所以都會先整理過
        return self.insertest(root,val)
        
def insertest(self, root, val):
        node = TreeNode(val)
        cur = root
        if cur.val:# 如果現在root是存在的話就繼續跑
            while cur:
            # 開始尋找要插進點的位置
                if node.val > cur.val:
                # 分類看是大於還是小於
                    if cur.right:
                    # 如果cur.right還存在就代表說還不是最底下
                        cur = cur.right
                    else:
                    # cur.right已經沒有，已經到達最底下了
                        return
                        #插進去右邊
                        self.addAtright(cur,node)
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        return self.addAtleft(cur,node)
        root.val = node.val
        # root不存在，所以就直接把root改為node的值
        return root
def addAtright(self,head,node) -> None:
    head.right = node

def addAtleft(self,head,node) -> None:
    head.left = node

```


## 整理
主要是每個動作執行前都會跑一次clean的動作
```python
def print(self,root,mylist):
    if root:
        mylist.append(root.val)
        self.print(root.left,mylist)
        self.print(root.right,mylist)
    return  mylist



def clean(self,root):

    mylist = []
    self.print(root,mylist)
    head = mylist[0]
    mylist.pop(0)
    nodetemp = TreeNode(head)
    for i in mylist:
        self.insertest(nodetemp,i)  
    root.val = nodetemp.val
    root.right = nodetemp.right
    root.left = nodetemp.left
    return root


def insertest(self, root, val):
    node = TreeNode(val)
    cur = root
    if cur.val:
        while cur:
            if node.val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    self.addAtright(cur,node)
                    return node
            else:
                if cur.left:
                    cur = cur.left
                else:
                    self.addAtleft(cur,node)
                    return node
    root.val = node.val
    return root

```

## 查詢

全部程式碼解釋
```python
def search(self,root,target):
        if root:# 先看root存在嗎？不存在就可以直接回傳None
            cur = root
            while target != cur.val:#開始尋找target
                if target > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        return None
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        return None
            print(cur)
            return cur
        else:
            return None

```

## 更改
```python
def modify(self, root, target, new_val):

    
        if self.search(root,target) == None:
        # 看是否要修改的值是存在的 如果不存在就回傳None
            return None
        else:
            self.clean(root)
            # 因為不確定樹是不是正確的，所以都會先整理過
            while self.search(root,target):
            # 如果找得到的話就代表有要修改的值，因為可能會是多個所以我是用迴圈
                self.search(root,target).val = new_val
                # 開始做修改
                self.clean(root)
                # 因為更改後可能會變成亂的所以又在重整一次
            return 

```