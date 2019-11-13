# Heap_sort 筆記




## 學習歷程：
想法：
陣列->Heapify->取出頭(min)->陣列中最尾放入頭->Heapify....


## 流程圖：

![](https://i.imgur.com/1xcTgnC.png)

繪圖工具：https://www.draw.io/



## 程式碼解析

>主要分成兩塊
`fun heap_sort`和`fun heapify`兩個function

`fun heap_sort`主要作用是在把陣列丟進`fun heapify`進行排列後取得第一個，持續跑迴圈直到list裡面沒有東西



`fun heapify`主要作用就是排列，把丟進來的list進行heapify，頭為最小。

### 各部分程式碼解析
#### heap_sort
主要由一個while迴圈組成，如果還有數值的話就持續跑迴圈。for裡面的會跑幾次是由幾個subtree來決定的。像是如果有三個數字的話就只用比較一次。
然後跑完所有的subtree比較後，就把頭刪掉，加進去自己創的新的list裡面。

```python=
        end = []
        while len(mylist)>0:
            for i in range((len(mylist)//2),0,-1):
                self.heapify(mylist,i)
            end.append(mylist[0])
            mylist.pop(0)   
        return end

```

#### heapify
subtree裡面的比較，如果endpoint是1的話，代表parent的位置是在list裡面的1(因為如果我不這樣寫會變成parent位置為1，寫成一行的方法還在想)。
再來就是定義subtree底下兩個left和right的位置。
比較的方法很簡單，就是如果比parent小就換位置
然後我會在裡面寫right如果不存在的話就回傳，因為如果我直接寫，就會一直說out of index，還在想辦法。
```python=
if(endpoint == 1):
        parent = 0
else:
        parent = endpoint//2+1
left = endpoint*2-1
right = endpoint*2

        if(mylist[left] < mylist[parent]):
            
            mylist[left],mylist[parent] =  mylist[parent],mylist[left]
        if(right> len(mylist)-1):
            return

        if( mylist[right] < mylist[parent]):
            
            mylist[right],mylist[parent] =  mylist[parent],mylist[right]


```


## 途中遇到問題

1. if(endpoint == 1):原本是只有 parent = endpoint//2+1
2. 

#### 一開始錯誤的程式碼
```python=

class Solution(object):
    def heap_sort(self, mylist):
        end = []
        while len(mylist)>0:
            for i in range((len(mylist)//2),0,-1):
                self.heapify(mylist,i)
            end.append(mylist[0])
            mylist.pop(0)   
        return end
    def heapify(self,mylist,endpoint):
        if(endpoint == 1):
            parent = 0
        else:
            parent = endpoint//2+1
        left = endpoint*2-1
        right = endpoint*2

        # left = parent*2+1
        # right = parent*2+2

        if(mylist[left] < mylist[parent]):
            mylist[parent],mylist[left] = self.swap(mylist[left],mylist[parent])
            # mylist[left],mylist[parent] =  mylist[parent],mylist[left]
        if(right> len(mylist)-1):
            return
            # mylist[right]!=None and
        if( mylist[right] < mylist[parent]):
            mylist[parent],mylist[right] = self.swap(mylist[right],mylist[parent])
            # mylist[right],mylist[parent] =  mylist[parent],mylist[right]

    def swap(self,a,b):
        # temp = a
        # a = b
        # b = temp
        return b,a
        # print(a,b)


list_test = [8,2,3,1,2,2,7,4,2]
# sol = Solution()

ans = Solution().heap_sort(list_test)

print(ans)

```
## 想要優化的點
1.交換的部分我想寫fun但是測試時一直有bug
2.if(right> len(mylist)-1):這行我一直想改掉，因爲很奇怪。但是我用其他方法都失敗。
3.空間的問題，應該是可以不用空間。
4.if(endpoint == 1):


## 全部程式碼


```python=

class Solution(object):
    def heap_sort(self, mylist):
        end = []
        while len(mylist)>0:
            for i in range((len(mylist)//2),0,-1):
                self.heapify(mylist,i)
            end.append(mylist[0])
            mylist.pop(0)   
        return end
    def heapify(self,mylist,endpoint):
        if(endpoint == 1):
            parent = 0
        else:
            parent = endpoint//2+1
        left = endpoint*2-1
        right = endpoint*2

        if(mylist[left] < mylist[parent]):
            
            mylist[left],mylist[parent] =  mylist[parent],mylist[left]
        if(right> len(mylist)-1):
            return

        if( mylist[right] < mylist[parent]):
            
            mylist[right],mylist[parent] =  mylist[parent],mylist[right]

 


list_test = [8,2,3,1,2,2,7,4,2,-1,33,22,100]
# sol = Solution()

ans = Solution().heap_sort(list_test)

print(ans)

```

## 參考資料
[[演算法] 堆積排序法(Heap Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php):主要看這個


[Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html):這次只有看一下下這個