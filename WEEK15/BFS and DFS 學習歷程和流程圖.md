# BFS and DFS 學習歷程和流程圖

## BFS流程圖以及程式碼解析以及學習歷程
>是以某一節點為出發點，先拜訪所有相鄰的節點。再依序拜訪與剛才被拜訪過的節點相鄰但未曾被拜訪過的節點，直到所有相鄰的節點都已被 拜訪過。 因此，進行 breadth-first search 時，需要使用 queue ，以便記錄拜訪的順序。

### 流程圖
![](https://i.imgur.com/rypRb88.png)

### 學習歷程
這次經過自己動手畫一次BFS的流程圖可以很快的寫出BFS的程式碼，唯一小卡住的地方是，一開始忘記檢查說temp(暫時)和cur(打印)要檢查兩個有沒有重複的值。

### 程式碼解析
```python
def BFS(self, s): 
        temp = []  #我區分為暫時的和要打印出的
        cur = []
        if self.graph[s]:#如果self.graph[s]有的話就代表個數字存在
            temp.append(s)
            #新增至暫時的list裡面
            while temp:#如果暫時的list還有東西就一直跑
                add = temp.pop(0)#這邊就是要打印出來的值為add
                cur.append(add)#將add加進去
                if self.find(add):#如果add有指向其他把它加進去temp
                    i = self.find(add)
                    for point in i:
                        if point in temp or point in cur:
                            pass
                        else:
                            temp.append(point)
                else:
                    pass
            print(cur)
            return cur
        else:
            return None

```
## DFS流程圖以及程式碼解析以及學習歷程
>depth-first search 是以某一節點為出發點，不斷地前進拜訪未曾被拜訪過的節點， 直到無路可走或是所有相鄰的節點都已經拜訪過為止，然後再退回前一個節點，尋找 沒有拜訪過的節點，直到所有相鄰的節點都已被拜訪過。 因此，進行 depth-first search 時，需要使用 stack ，以便記錄所走過的路徑。
>

### 流程圖
![](https://i.imgur.com/EJAUnGM.png)

### 學習歷程
一開始比起BFS卡比較久因為不太懂他的流程，最後是在看一次老師的youtube中是說一樣是把它放進temp(暫時)，然後只是是先刪除掉尾巴因為是stack的方法這樣。

### 程式碼
大致上都跟BFS一樣，只是一個是queue的概念一個是stack,DFS是stack所以在pop的部分就是刪掉尾巴這樣
```python
    def DFS(self, s):
        temp = []    
        cur = []
        if self.graph[s]:
            temp.append(s)
            while temp:
                add = temp.pop()
                #和BFS不一樣的地方，是刪除尾巴
                cur.append(add)
                if self.find(add):
                    i = self.find(add)
                    for point in i:
                        if point in temp or point in cur:
                            pass
                        else:
                            temp.append(point)
                else:
                    pass
            print(cur)
            return cur
        else:
            return None
```



## 參考資料

[縱向優先搜尋 (depth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dfs.html)

[橫向優先搜尋 (breadth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html)

[老師moodle](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_5)

[老師的youtube影片](https://www.youtube.com/watch?v=DBnB60IOiw8&feature=youtu.be)