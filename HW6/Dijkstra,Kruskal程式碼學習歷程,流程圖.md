# Dijkstra
>該演算法的輸入包含了一個有權重的有向圖 G，以及G中的一個來源頂點 S。我們以 V 表示 G 中所有頂點的集合。每一個圖中的邊，都是兩個頂點所形成的有序元素對。(u, v) 表示從頂點 u 到 v 有路徑相連。我們以 E 表示G中所有邊的集合，而邊的權重則由權重函式 w: E → [0, ∞] 定義。因此，w(u, v) 就是從頂點 u 到頂點 v 的非負權重（weight）。邊的權重可以想像成兩個頂點之間的距離。任兩點間路徑的權重，就是該路徑上所有邊的權重總和。已知 V 中有頂點 s 及 t，Dijkstra 演算法可以找到 s 到 t 的最低權重路徑(例如，最短路徑)。這個演算法也可以在一個圖中，找到從一個頂點 s 到任何其他頂點的最短路徑。
>
在寫作業途中遇到最大點就是我在cur,temp那邊設變數有點混亂。所以答案時常會不一樣。
## Dijkstra 流程圖
![](https://i.imgur.com/EA7SDod.png)

## Dijkstra程式碼說明
```python
def Dijkstra(self, s): 
        unvisit = [i for i in range(len(self.graph))]  #尚未走過的點     
        path = {} #代表每個點到其他點的路徑
        for i in range(len(self.graph)): # 開始初始化，路徑
            path[i] = None
        path[s] = 0
        while unvisit != []:# 若有還沒有的採訪點就要持續跑迴圈
            temp = self.temp_dic(unvisit,path) # 找出剩餘要走的路徑
            cur = self.find_min(temp) #找出當前點的最小點
            unvisit.pop(unvisit.index(cur)) 
            for index,i in enumerate(self.graph[cur]): # 開始跑當前最小點，然後繼續往前，以及更新
                if i != 0:# 如果不為0才代表有連結
                    if path[index] == None: # 如果是none的index就加上 連接點和他們之間的距離

                        path[index] = path[cur] + i
                    else:
                 
                        if path[cur] + i < path[index]:
                            path[index] = path[cur] + i # 如果比較小就需要更新

                else:
                    continue

        return path
    def temp_dic(self,unvisit,path): # 這個函式就是找出剩餘要走的路徑
        temp = {}
        for j in unvisit:
            temp_add = {j:path[j]}
            temp.update(temp_add)
        return temp
    def find_min(self,path): # 這個函式是找出最小的點在temp路徑中

        smallest =  min(path[x] for x in path if path[x] is not None)
        for v in path:
            if path[v] == smallest:
                smallest_key = v
            else:
                continue

        return smallest_key 

```

## Dijkstra學習歷程

- 錯誤1 關於更新時一開始index的寫法是錯誤    
一開始寫更新時，原本是這樣寫，是錯誤的
```python
if path[index+1] == None:
    path[index+1] = i

```

- 錯誤2 在找尋min那邊一開始寫成min(path)，但是後來發現這樣回返回None有時候所以要做更改

原本：
```python
    def find_min(self,path):
        smallest = min(path)
        return smallest

```

更動後：不僅僅先找出最小值，寫說is not none在尋找時，也可能會因為值一樣就返回。
```python
def find_min(self,path):

        smallest =  min(path[x] for x in path if path[x] is not None)
        for v in path:
            if path[v] == smallest:
                smallest_key = v
            else:
                continue

        return smallest_key 

```
- 錯誤3

- 縮短程式碼1
原本是用if,else所以會看起來很長
```python
for i in range(len(self.graph)):
            if i == s:
               path[i] = 0
                new = {i:0}
                path.update(new)
            else:
               path[i] = None
                new = {i:None}
                path.update(new)

```

更改後： 就只用更改s這個點就好
```python
for i in range(len(self.graph)):
            path[i] = None
        path[s] = 0
```

# Kruskal 
>Kruskal演算法是一種用來尋找最小生成樹的演算法
>最小生成樹(Minimum Spanning Tree)
在無向圖有權重的連通圖中找尋可以連接所有點的邊且不形成循環，且這些邊的權重和最小，可以連通所有點且不形成循環，一定會形成樹，這樣的問題稱作最小生成樹(Minimum Spanning Tree)。


## Kruskal 流程圖
![](https://i.imgur.com/GCkqMnr.png)


## Kruskal 程式碼說明
```python
def Kruskal(self):
        final = {} #為最後要回傳的dic
        unvisit = [i for i in range(len(self.graph_k))]       #建立一個還未走到的list
        temp = {} # 為還沒走過的路徑
  
        for i in range(len(self.graph_k)):
            for index,j in enumerate(self.graph_k[i]):
                if j != 0:
                    temp[j] = [index,i] #開始建立temp path

        while unvisit != []: #如果還有為走過的 就一直跑回圈
            
            cur = self.find_min_edge(temp) #有一個額外的 def 可以幫忙找尋目前最距離

            new = {} #把他加入
            final.update(cur)
            for  key,value in cur.items():
                key_del = key
                value_del = value #這邊為找到key和value cur的
            temp.pop(key_del)
            unvisit.pop(0)  
        final_return = {} #回傳final_return 因為格式要修正
        for key,value in final.items():
            new = {str(value[1])+'-'+str(value[0]):key}

            final_return.update(new)
        print(final_return)
        return final_return
    def find_min_edge(self,path):

        temp = min(path)
        min_edge = {}
        min_edge[temp] = path[temp]

        return min_edge

```

## Kruskal 學習歷程
錯誤
```python
def Kruskal(self):
        """
        :rtype: dict
        """
        # 開始某次找罪小的權重然後要注意不能有cycle
        # 每個點都有3次機會
        # stop = [i for i in range(len(self.graph_k))]*3
        # stop.sort()

        # stop.pop(stop.index(2))

        stop = {}
        for i in range(len(self.graph_k)):
            stop[i] = 3

        final = {}
        unvisit = [i for i in range(len(self.graph_k))]       
        temp = {}
        #建立初始temp當作搜尋用
        for i in range(len(self.graph_k)):
            for index,j in enumerate(self.graph_k[i]):
                if j != 0:
                    temp[j] = [index,i]

        # for i in range(len(self.graph_k)):
        while unvisit != []:
            
            cur = self.find_min_edge(temp) 
            for i in range(len(self.graph_k)):
                if stop[i] <= 1:
                    break
                # else:
            new = {}
            final.update(cur)
            # print(cur)
            
            for  key,value in cur.items():
                key_del = key
                value_del = value
            temp.pop(key_del)
            stop[value_del[0]] = stop[value_del[0]]-1
            stop[value_del[1]] = stop[value_del[1]]-1
            # stop.pop(stop.pop(value_del[0]))
            # stop.pop(stop.index(value_del[1]))
            unvisit.pop(0)
            
        final_return = {}
        for key,value in final.items():
            new = {str(value[1])+'-'+str(value[0]):key}
            # final_return[value[0]] = key
            final_return.update(new)
        print(final_return)
        return final_return
    def find_min_edge(self,path):
        #開始找最小的
        # min_edge = min(path)
        # print(path)
        # a = {10: [1, 0], 6: [2, 0], 5: [3, 0], 15: [3, 1], 4: [3, 2]}
        temp = min(path)
        min_edge = {}
        min_edge[temp] = path[temp]

        return min_edge

g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()



# a = [1,2,3]
# b = [0,1,2]
# while a != []:
#     for i in b:
#         if i == 1:
#             break  
#         else:
#             print(i)
#     a.pop()    
#     print('hi')



# a ={ 2: None, 3: 1, 4: None}
# smallest =  min(a[x] for x in a if a[x] is not None)
# print(smallest)
# for v in a:
#     if a[v] == smallest:
#         print(v)
#     else:
#         print('s')
# a = [2,3,4,1,6]
# for x,y in enumerate(a):
#     print(x,y)
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
```

# 參考資料
[Single-Source Shortest Path：Dijkstra's Algorithm](http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html)

[Graph Data Structure 4. Dijkstra’s Shortest Path Algorithm](https://www.youtube.com/watch?v=pVfj6mxhdMw)

[維基百科](https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)

[圖形演算法-最小生成樹](https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu)

[克魯斯克爾演算法](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)

[Kruskal](https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu)