# Merge_sort筆記

## 學習歷程：
在途中遇到最困難的點就是遞迴關係，一開始有點想不透。就是其他如何對掉那些我覺得還好。但是要如何切割完最小後再返回去就有點不了解。


以下是我用寫的流程圖，只有寫左半邊。
未來有空再用電腦畫。
![](https://i.imgur.com/ZJQjSu9.jpg)


## 流程圖：
![](https://i.imgur.com/YYEtCPq.png)

繪圖工具：https://code2flow.com/
第一次用的有點不上手


## 程式碼解析

>主要分成兩塊
`fun merge_sort`和`fun merge`兩個function

`fun merge_sort`主要是說區分mylist然後一直切割切割切到你只剩下自己再慢慢往回推
`fun merge`就很簡單，就是你有左和右邊的list每次各取一個點進行得比較。

### 各部分程式碼解析
#### merge_sort
是由一個if和else所構成。主要概念，就是慢慢把mylist切割切到你只剩下自己本身就可以開始往上回推了。

可以看到一個`left`和`right`，就是會讓裡面的list一直重複這個切割，直到跑進if裡面的return 才會進入到 `fun merge`這個階段。
然後跑回來的newlist就會進入到之前的位置，和別人進行`fun merge`。直到最後
```python=
        if len(mylist) == 1:
            return mylist
        else:
            left = self.merge_sort(mylist[0:(len(mylist)//2)])
            right = self.merge_sort(mylist[(len(mylist)//2):])
            newlist = self.merge(left,right)
            return newlist

```

#### merge
這個排序的想法就非常簡單，由一個while所構成。
跳出while就是當你的左邊或是右邊的長度等於0的時候。(一開始這邊一直設錯)

分類主要是每次選左邊和右邊的第一個點開始進行比較，比較比較小的就加進去`temp`，直到有一個地方為0。

之後再把剩下的left或是right加進去。
不需要擔心說如果把剩下的加進去大小會不會亂掉，你已經比較過左右兩邊裡面list的排列順序，所以不用擔心。
把剩下的值加進去是用`extend`而非`append`當時候犯錯造成裡面超級多個list。
```python=
 temp = []
        a = right[0]
        b = left[0]
        while len(right) != 0 and len(left) !=0:
            a = right[0]
            b = left[0]
            if a<b:
                temp.append(a)
                right.pop(0)
            else:
                temp.append(b)
                left.pop(0)
        temp.extend(left)       
        temp.extend(right)
        return temp 

```



## 途中遇到問題

1. 把剩下的值加進去是用extend不是append
2. merge裡面的while條件式
不是len(right) == 0 or len(left)==0:(這樣永遠不會跳進去)
3. 在while裡面的a和b應該是寫在while的底下而非上面，寫在底下是因為每次都已經把right和left的頭要刪的刪掉了

#### 一開始錯誤的程式碼
```python=
class Solution:
    def sort(self,mylist):
        if len(mylist) <= 1:
            return mylist
        else:
            left = self.sort(mylist[0:(len(mylist)//2)])
            right = self.sort(mylist[(len(mylist)//2):])
            newlist = self.merge(left,right)
            return newlist
    def merge(self,left,right):
        temp = []
        # temp_len = len(right)+len(left)
        # a = right[0]
        # b = left[0]
        while len(right) == 0 or len(left)==0:
            a = right[0]
            b = left[0]
            if a<b:
                temp.append(a)
                right.pop(0)
                a += 1
            else:
                temp.append(b)
                left.pop(0)
                b += 1
        # temp.append(left)
        temp.extend(left)
        temp.extend(right)
        return temp

```

## 全部程式碼


```python=
class Solution(object):
    def merge_sort(self, mylist):
        if len(mylist) == 1:
            return mylist
        else:
            left = self.merge_sort(mylist[0:(len(mylist)//2)])
            right = self.merge_sort(mylist[(len(mylist)//2):])
            newlist = self.merge(left,right)
            return newlist
    def merge(self,left,right):
        temp = []
        a = right[0]
        b = left[0]
        while len(right) != 0 and len(left) !=0:
            a = right[0]
            b = left[0]
            if a<b:
                temp.append(a)
                right.pop(0)
            else:
                temp.append(b)
                left.pop(0)
        temp.extend(left)       
        temp.extend(right)
        return temp 



```

## 參考資料
[合併排序法(Merge Sort) @ 小殘的程式光廊:: 痞客邦::](https://emn178.pixnet.net/blog/post/87965707):
我是看他的pesudo code我覺得不錯

[Comparison Sort: Merge Sort(合併排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html):我每次學演算法都會看他的，但文字小多