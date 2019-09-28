# WEEK1-Codesignal

[TOC]


## 把一串字中多餘空格刪除再來重新排列(13題)

用到觀念
- `split('')`
- `join('')`

split() 透過指定分隔符號對字串進行切割

注意！
**`split()`函数默认可以按空格分割，並且把结果中的空字符串删除掉，留下有用信息**
如果使用`split(' ')`，則會把空格都計算進去，要注意


```python=
a = "def      m   e"
b = a.split(' ')
# b = ['def','','','','','','m','','','e',]

a ="def      m   e"
c = a.split()
#c = ['def', 'm', 'e']
```

`join()`將序列指定字產生一個新的字串


```python=
#這題回答

def catWalk(code):
    return ' '.join(code.split())

#將code那些先切割，因為依照split默認，所以會把多餘空格刪除
#再來用join每一個字後面新增一個空格。

```
