# Binaray Search Tree
分為主要
- insert 
- delelte
- search
- modify 

### 前言
這次寫BST最主要花的時間是在刪除和整理，其他則是蠻快想出來的。而整理最後還是對於pointer的概念太薄弱所以一直寫錯，所以我認為我得重新再認識一次pointer才行。

:::spoiler 簡單講述Binary Tree
簡單來說就是tree的延伸，最主要就是節點只有2個(你的child)
### 組織
- `root` 最頂端->你沒有parent就是root
- `parent `你那個區域的頂端
- `child` 區域的底下
- `Edge` The connection between one node and another.
- `level` 1 + the number of edges between a node and the root, i.e. (Depth + 1)
- `path`A sequence of nodes and edges connecting a node with a descendant.
- `depth`The distance between a node and the root.

:::

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
## 刪除
### 流程圖
![](https://i.imgur.com/obFtWkT.png)
### 學習歷程
寫最最久的一個，途中遇到很多問題，像是完全不知道要怎麼刪除，一開始困惑很久說到底流程是什麼

一開始錯誤的程式碼，一開始我是想先找到那個點
但是點是指上一個點，這樣的話就可以把上一個點指派給下下一個
```python
cur = self.root
while target != cur.right.val or target != cur.left.val:
    if target > cur.val:
        cur = cur.right
    else:
        cur = cur.left
if target == cur.right.val:
    end = cur.right#target
    if end.right==None and end.left==None:
        cur.right == None
    elif end.right==None:
        cur.left = end.left
    elif end.left==None:
        cur.right = end.right
    # else:
        #case 3 找出右邊最小的替代
else:
    end = cur.right#target
    if end.right==None and end.left==None:
        cur.right == None
    elif end.right==None:
        cur.left = end.left
    elif end.left==None:
        cur.right = end.right
    # else:

```
可能情況
- 底下沒有東西->直接刪！
- 底下只有一個子結點
- 底下有左右兩個子結點
https://www.youtube.com/watch?v=pYT9F8_LFTM

## 更改
### 學習歷程
原本想法
把所有要修改的值都先刪掉 再來做insert進去
但是我想想後覺得太愚蠢，而且花的時間這樣是跑兩次O(logn)的樣子那該算邊搜尋邊更改。
後來在11/22要睡覺前想到，就是使用search的方法來使用，因為search是會回傳node所以我就可以更改他的.val就可以
程式碼也很簡單




### 需要思考的地方，需要查查
- [ ] moderate time是什麼？
- [x] ask 助教空的root是什麼時候像是node(None?)
- [ ] python deepcopy and copy

好用快捷鍵
### 同時選取相同名稱的字串
###  需要統一修改特定的字串時，可以先選取其中一個，再透過下面的方式選取同樣的字串，就能一次修改
Ctrl + F2
Ctrl + Shift + L

學到的小東西
在解决方案函数下面有一些注释
type:    Type of a parameter.
vartype: Type of a variable. 
rtype:   Return type. 

## Ref.

[Tree系列文章](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)他整理的真的很好，看了一下delete的觀念(因為我不是很懂)





