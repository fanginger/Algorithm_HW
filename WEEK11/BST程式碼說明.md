# Binaray Search Tree 程式碼功能說明
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

## 刪除
>主要分為`func delete`和`func delete_2`
由`func delete` 來看是否還有要進行修正的
由`func delete_2`來進行修改


`func delete` 部分
```python
def delete(self,root,target):
        while self.search(root,target):
        # 如果有就代表有要修正的
            self.delete_2(root,target)
        return root
        # 沒有要修正，返回root
```
`func delete_2`部分
```python
def delete_2(self, root, target):
        if root == None: 
            return root  
  
        if target < root.val: 
            root.left = self.delete_2(root.left,target) 

        elif(target > root.val): 
            root.right = self.delete_2(root.right, target) 
    
        else:  
            # 現在的root就是為target所以可以進行刪除了
            if root.left == None and root.right == None:# case1，底下都沒有點，回傳none讓他接回去
            
                root = None
                return None

            if root.left == None : # case2 底下會有 一個節點，左邊或是右邊
                return root.right  
                # 如果左邊為none代表是右邊才有值所以回傳root的right
                
            if root.right == None : 
                return root.left  
    
            else:
            #case3
                temp = root.left
                # 現在要開始找左邊最大
                while root.right:
                    temp = temp.right
                # 找到最大值後把root的val替換掉
                root.val = temp.val 
                # 再把temp刪除但是要把right的
                root.right = self.delete_2(root.right , temp.val) 

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
                # 開始比大小
                    if cur.right:
                    #如果cur.right還有東西，代表還沒有到最底
                        cur = cur.right
                    else:
                    # 如果已經沒有代表根本沒有這個值
                        return None
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        return None
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


## Ref.

[Tree系列文章](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)他整理的真的很好，看了一下delete的觀念(因為我不是很懂)
[Binary Search Tree | Set 2 (Delete)](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/) 看了他的delete 因為在寫case3時會遇到問題，所後看了一下，還是跟遞迴是有關聯的。所以之後可能再次複習遞迴或是多加練習。
[youtube影片](https://www.youtube.com/watch?v=pYT9F8_LFTM)再次建立delete觀念
與朋友討論整理這部分要怎麼寫，討論時間約10分鐘。最後他提醒我要用pointer的想法，因為我那時候就是想說可以使用等號就可以把整顆樹複製過去，但是這樣會產生一個問題，就是我是建立一顆新的樹。所以他給我的建議是要用pointer。無程式碼上面的實質幫助。
[pointer的概念](https://michaelchen.tech/c-programming/pointer/)
