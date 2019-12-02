# Hash Table


## Hash table(雜湊表，哈希表)原理
## Hash Function(雜湊函式) 原理
>目的是：雜湊函式把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定(長度...)下來。
方法是：主要就像是下方的圖一樣，你輸入一個值後，經過Hash function 的轉換 就會轉變成一個新的雜湊值（hash values，hash codes，hash sums，或hashes）
![](https://i.imgur.com/hF5bdON.png)


通常你輸入不同的值進去，經過Hash function 後得到的雜湊值會是不一樣的。但是有例外，如雜湊碰撞（collision）。
###  理想的密碼雜湊函式
- 對於任何一個給定的訊息，它都很容易就能運算出雜湊數值。
- **難以**由一個已知的雜湊數值，去推算出原始的訊息。
- 在不更動雜湊數值的前提下，修改訊息內容是不可行的。
- 對於兩個不同的訊息，它不能給與相同的雜湊數值。
    - 意外：雜湊碰撞（collision）

### 常見密碼雜湊函式
- MD5訊息摘要演算法
    - 產生出一個128位元（16位元組）的雜湊值（hash value）
### 應用
- 保護資料
- 雜湊表：能夠快速的按照關鍵字尋找資料記錄。
- 錯誤校正
- Rabin-Karp字串搜尋演算法

## 流程圖與程式碼解析
### Add
![](https://i.imgur.com/JzzcIez.png)
```python
 def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        h = MD5.new()
        h.update(key.encode('utf-8'))
        x = int(h.hexdigest(),16)
        # 轉換為10進位
        put_to = x%5
        # print(x%5)
        node = ListNode(key)
        if self.data[put_to]:
            #先找有沒有存在
            # 開始找最尾巴
            cur = self.data[put_to]
            while cur:
                if cur.next != None:
                    cur = cur.next
                else:
                    cur.next = node
                    return
        else:
            
            self.data[put_to] = node
            return 

```

### Find、Contain
![](https://i.imgur.com/pDeViiG.png)
```python
def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        if self.find(key) == None:
            return 
        else:
            if self.find(key).next != None:
                cur = cur.next 
                return 
            else:
                cur = self.find(key)
                cur.val = None
                # self.find(key).val = None
                return

```
Find
```python
def find(self, target):
        for i in range(0,self.capacity):
            root = self.data[i]
            if root:
                cur = root
                while cur:
                    if cur.val == target:
                        print(cur.val)
                        return cur
                    elif cur.next != None:
                        cur = cur.next
                    elif cur.next == None:
                        break
            else:
                pass
        print(None)
        return None

```
### 刪除
```python
def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        if self.find(key) == None:
            return 
        else:
            if self.find(key).next != None:
                cur = cur.next 
                return 
            else:
                cur = self.find(key)
                cur.val = None
                # self.find(key).val = None
                return

```

## 學習歷程

### break、pass、continue
途中有一部部分在find那邊遇到一個問題
```python
for i in range(0,self.capacity):
    root = self.data[i]
    if root:
        cur = root
        while cur:
            if cur.val == target:
                print(cur.val)
                return cur
            elif cur.next != None:
                cur = cur.next
            elif cur.next == None:
                break
                # 這邊就會跳出此次迴圈，就是while cur
                # 跑到 i += 1 的新迴圈
```
在break那邊原本打成pass 我是原本想說他就會跳出去但是他會一直跑迴圈什麼都不做，後來上網查跳出此次迴圈要使用break

整理

>break：強制跳出 ❮整個❯ 迴圈
continue：強制跳出 ❮本次❯ 迴圈，繼續進入下一圈
pass：不做任何事情，所有的程式都將繼續，一種中助詞

範例：
```python
for k in range(3):
    for i in range(5):
        if i == 2:
            break    
        if i == 0:
            pass
            print('hi')
        if i == 1:
            continue
            print('1')
```
結果
```python
hi
```
到了0，經過pass什麼都不會發生。->所以會印出hi
到了1，經過continue跳出本次迴圈所以不會印出1，跑到i == 2
到了2，經過break，直接跳出當前迴圈跑到上一層迴圈，所以會跑到k = 2

## Ref.
[wiki-雜湊函式](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8)
[wiki-MD5](https://zh.wikipedia.org/wiki/MD5)
[1 分鐘搞懂 Python 迴圈控制：break、continue、pass](https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8)
