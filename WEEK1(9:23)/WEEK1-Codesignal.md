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


## 替換(題目14)
使用語法：`replace()`

str.replace(old, new[, max])
- old 要被替換的
- new 心得
- max 最多不能替換多少格

範例：
```python=
str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);

#thwas was string example....wow!!! thwas was really string
#thwas was string example....wow!!! thwas is really string

```

題目回答：
```python=
def convertTabs(code, x):
    return code.replace('\t'," " * x)

#要轉換的是'\t' 換成 ' '乘幾個x
```
