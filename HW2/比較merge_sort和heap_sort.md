

### 時間複雜度上面
![](https://i.imgur.com/PidsgNI.png)
在時間複雜度上面是一樣的

### 測試比較
使用隨機產生數字的方法
1~1000跑10000個資料看哪個比較快速
```python=
import random
import numpy as np
x = np.random.randint(1,1000,10000)
#隨機生成數字
list_test = x.tolist()

```


結果：
第一次
merge sort
![](https://i.imgur.com/MPCmcxC.png)
heapsort
![](https://i.imgur.com/zoUlwGh.png)

第二次
merge sort
![](https://i.imgur.com/YexvSGZ.png)
heapsort
![](https://i.imgur.com/Lntqnpf.png)

關於heap sort 和merge sort時間上面的解釋
>Although time complexity is the same, the constant factors are not. Generally merge sort will be significantly faster on a typical system with a 4 or greater way cache, since merge sort will perform sequential reads from two runs and sequential writes to a single merged run. I recall a merge sort written in C was faster than an optimized heap sort written in assembly.(取自網友解釋)

大概意思是指(翻譯資質駑鈍請看原文)：雖然時間複雜度兩者都是一樣的，但是實際的因素卻是不一樣。在一班情況mergesort會比較快在一般的裝置上面(with 4 way cache(四個快取塊))


#### 關於上文提到的快取
CPU快取
在電腦系統中，CPU快取（英語：CPU Cache，在本文中簡稱快取）是用於減少處理器存取記憶體所需平均時間的部件。在金字塔式記憶體階層中它位於自頂向下的第二層，僅次於CPU暫存器。其容量遠小於記憶體，但速度卻可以接近處理器的頻率。

### 參考資料
[heapsort和mergesort圖片取自](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)

[Heap Sort vs Merge Sort in Speed [duplicate]
](https://stackoverflow.com/questions/53269004/heap-sort-vs-merge-sort-in-speed)

[wiki-CPU快取](https://zh.wikipedia.org/wiki/CPU%E7%BC%93%E5%AD%98)