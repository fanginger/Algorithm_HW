# Binaray Search Tree 流程圖、學習歷程
作業分為主要
- insert 
- delelte
- search
- modify 
- clean(整理)

### 前言
這次寫BST最主要花的時間是在刪除和整理，其他則是蠻快想出來的。而整理最後還是對於pointer的概念太薄弱所以一直寫錯，所以我認為我得重新再認識一次pointer才行。


>簡單來說就是tree的延伸，最主要就是節點只有2個(你的child)
>### 組織
>- `root` 最頂端->你沒有parent就是root
>- `parent `你那個區域的頂端
>- `child` 區域的底下
>- `Edge` The connection between one node and another.
>- `level` 1 + the number of edges between a node and the root, i.e. (Depth + 1)
>- `path`A sequence of nodes and edges connecting a node with a descendant.
>- `depth`The distance between a node and the root.



## 新增
### 流程圖
前面沒有加入整理
![](https://i.imgur.com/6erN657.png)

### 學習歷程
其實光只有insert沒有花太多時間，所以就不加多說。因為寫過linked list所以這部分寫蠻快的


## 尋找
### 流程圖

![](https://i.imgur.com/uYEHqZo.png)

### 學習歷程
我覺得跟寫新增時差不多流程，想法差不多
>卡比較久的地方是在我一開始找點時候，我寫成如果還有右邊就一直尋找這樣根本不是每到一個新的cur就比較一次
>
就會跑到最右邊的點
![](https://i.imgur.com/Z0nYKPK.png)

```python
while target != cur.val:
            if target > cur.val:
                while cur.right:
                    cur = cur.right
                return False                 
            else:
                while cur.left:
                    cur = cur.left
                return False   
        return cur

```
正確寫法:boom:
只要把while cur.right改成if cur.right
```python
while target != cur.val:
            if target > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    return False
            else:
                if cur.left:
                    cur = cur.left
                else:
                    return False
        print(cur)
        return cur

```


## 刪除
### 流程圖
![](https://i.imgur.com/obFtWkT.png)
### 學習歷程
寫最最久的一個，途中遇到很多問題，像是完全不知道要怎麼刪除，一開始困惑很久說到底流程是什麼

一開始錯誤的程式碼，一開始我是想先找到那個點
但是點是指上一個點，這樣的話就可以把上一個點指派給下下一個


原本一開始錯誤的程式碼
```python
cur = self.root
while target != cur.right.val or target != cur.left.val:
    if target > cur.val:
        cur = cur.right
    else:
        cur = cur.left
if target == cur.right.val:
    end = cur.right
    if end.right==None and end.left==None:
        cur.right == None
    elif end.right==None:
        cur.left = end.left
    elif end.left==None:
        cur.right = end.right

else:
    end = cur.right
    if end.right==None and end.left==None:
        cur.right == None
    elif end.right==None:
        cur.left = end.left
    elif end.left==None:
        cur.right = end.right


```
可能情況
- 底下沒有東西->直接刪！
- 底下只有一個子結點
- 底下有左右兩個子結點


## 更改
### 學習歷程
原本想法
把所有要修改的值都先刪掉 再來做insert進去
但是我想想後覺得太愚蠢，而且花的時間這樣是跑兩次O(logn)的樣子那該算邊搜尋邊更改。

原本的想法，是可行的但是就是太麻煩
#### 流程圖(初始想法的)
![](https://i.imgur.com/oLJIZAj.png)

後來在11/22要睡覺前想到，就是使用search的方法來使用，因為search是會回傳node所以我就可以更改他的.val就可以，程式碼也很簡單
流程就簡單許多。
### 流程圖(最終)
![](https://i.imgur.com/dICpP0A.png)


## 整理
### 學習歷程
雖然這不是在要繳交作業的範圍內，但是因為每一個部分在你執行前，助教可能會給你一顆亂樹。所以都應該先跑一次整理的部分，在很多地方都也有用到。像是modify在結束後面都會使用到clean所以我認為這個我有點想寫出來。

> 而且這部分算是我遇到問題很多很多的地方

首先，**這是最重要的**!
得建立pointer的概念，我是觀看其他人的文章，底下有連結或是[點擊](https://michaelchen.tech/c-programming/pointer/)
>指標 (pointer) 是 C (或 C++) 中用來管理記憶體的語法特性，指標內儲存的值 (value) 是記憶體的虛擬位置 (virtual address)。

之後的再補。。目前還在寫delete的程式碼
### 學到的小東西
1. 程式碼的函式註解
```python
type:    Type of a parameter.
vartype: Type of a variable. 
rtype:   Return type. 

```
2. 快捷鍵
**同時選取相同名稱的字串**
需要統一修改特定的字串時，可以先選取其中一個，再透過下面的方式選取同樣的字串，就能一次修改
Ctrl + F2
Ctrl + Shift + L
我是用mac所以是Cmd + Shift + L


### 途中遇到的問題。需要思考的地方，需要查查
- [ ] moderate time是什麼？
- [x] ask 助教空的root是什麼時候像是node(None?)
- [ ] python deepcopy and copy
- [ ] preoder 列印之類的
- [ ] 遞迴練習

## Ref.

[Tree系列文章](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)他整理的真的很好，看了一下delete的觀念(因為我不是很懂)
[Binary Search Tree | Set 2 (Delete)](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/) 看了他的delete 因為在寫case3時會遇到問題，所後看了一下，還是跟遞迴是有關聯的。所以之後可能再次複習遞迴或是多加練習。
[youtube影片](https://www.youtube.com/watch?v=pYT9F8_LFTM)再次建立delete觀念
與朋友討論整理這部分要怎麼寫，討論時間約10分鐘。最後他提醒我要用pointer的想法，因為我那時候就是想說可以使用等號就可以把整顆樹複製過去，但是這樣會產生一個問題，就是我是建立一顆新的樹。所以他給我的建議是要用pointer。無程式碼上面的實質幫助。
[pointer的概念](https://michaelchen.tech/c-programming/pointer/)



