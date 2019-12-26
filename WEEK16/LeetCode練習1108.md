# LeetCode練習1108
## 1108. Defanging an IP Address
難度:easy

題目:
>Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
>
測資：
>Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


時間:12:40-12:45

想法:這題其實如果用內建的轉換會非常簡單，因為我前幾天才用replace所以我看到這題就想說應該是可以用。之後再想想不用此內建函數的方法。


我的程式碼:
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = address.replace('.','[.]')
        return new
        
```

若不想要用內建函數:
在建立一個新的字串，然後加入
```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        new =''
        for i in address:
            if i == '.':
                new  += '[.]'
            else:
                new += i
        return new
        

```