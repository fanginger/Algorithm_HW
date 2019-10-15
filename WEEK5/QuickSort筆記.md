# Quick Sort
## 前言


![](https://i.imgur.com/r8HQm8p.png)

best 就是最好的情況
->比較qucik sort 和 insertion sort 因為insertion可以跑一次就可以跑完全部
大部分比較都是average 或是 worst

## 想法概念




選擇一個pivot點，然後依序將剩餘的數字排列
pivot的選擇可以是任意的，我是選擇最後一個


![](https://i.imgur.com/MstZ21N.png)


>將其大於pivot的數字放置右邊成為一個新的list，將小於的數字放置左邊，也成為新的list。
重複上述步驟，直到分不出來就停下。(遞迴觀念)

![](https://i.imgur.com/kyMwXNX.png)


## 程式架構

![](https://i.imgur.com/GDGMrVO.png)


### Partition 分類


#### 定義變數
在`partition function`裡面
- `int front`代表每組list的最前頭，一開始初始為0
- `int end`代表最後一個，同時也是pivot位置，一開始為len(list)-1
- `int i`代表最後一個指到的比pivot還小的值，所以i旁邊都是比pivot還要大的值
- `int j`為比pivot還要大的最後一個值



![](https://i.imgur.com/JTbut3T.png)
因為front<end，所以開始區分。
在這裡選定尾巴當作pivot開始區分左右兩堆
丟進partition的function裡面



![](https://i.imgur.com/75c5n29.png)
```python=
def partition(self,mylist,front,end):
        i = front-1
        j = front
        pivot = mylist[end]
        while j < end:
            if(mylist[j]>pivot):
                j +=1
            else:
                i+= 1
                mylist[j],mylist[i] = mylist[i],mylist[j]
                j+=1
        i+=1
        mylist[j],mylist[i] = mylist[i],mylist[j]
        return i 

```

這代表假如左邊有值就繼續進行這個迴圈
然後區分兩堆
一堆為比pivot大的 (if)
另一堆為比pivot小的(else)

![](https://i.imgur.com/he9wHEv.png)

#### j <pivot時

現在第一個點3<4：
所以進行
```python=
        i+= 1
        mylist[j],mylist[i] = mylist[i],mylist[j]
        j+=1

```

把i這個變數往右移一格，代表多一格位置給比pivot小的 位置
再來交換j和ｉ值因為j代表現在所指的位置，所以要交換
最後j再加一前進

#### j > pivot時
![](https://i.imgur.com/WafHeGZ.png)
現在第二個點8>4

```python=
        j+=1
```

直接j+=1因為也不需要變動到什麼改變什麼位置
因為j都是代表比pivot還要大的值

#### 到最尾巴 j = pivot時

![](https://i.imgur.com/y5l52Dd.png)
```python=
     i+=1
     mylist[j],mylist[i] = mylist[i],mylist[j]
     return i 
```
最後把pivot加進list裡面排列
將 i 值加一往後退一格給pivot放，在交換i的值和pivot的值

最後回傳 `int i `即是pivot的位置

在區分時會使用到
```python=
self.sortList(mylist,front,pivot-1)
            #左邊的list 頭到pivot的前一個
self.sortList(mylist,pivot+1,end)
            #右邊的list pivot的後一個到最尾巴

```


### 使用工具
畫流程圖：https://www.draw.io
手繪亂亂的：aww







