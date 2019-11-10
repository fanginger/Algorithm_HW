# CS50 WEEK 5(HTTP)
## HTTP(Hypertext Transfer Protocol)
>是一個應用層協定(application layer protocols)，可以從client端向server端進行requeest的一個protocol(協定)。

忘記請看[OSI模型](https://zh.wikipedia.org/wiki/OSI%E6%A8%A1%E5%9E%8B)各種層級協定

比較：HTTPS, 更加安全的通訊方法


### Other application layer protocols inculiding:
- FTP
- SMTP(simple mail transfer protocol)
- DDS(data distibution servie)
- RDP
- XMAPP

HTTP/1.1
我在使用version為1.1的HTTP
就只是the format of the protocol
也有1.0但是現在很少被使用


## The basic of what a protocol request


![](https://i.imgur.com/CdmCtem.png)
`GET`是一種我們要向網頁做出什麼樣的舉動
常見的為：
- GET
- POST
- PUT
- DELETE
`/`為只說我們要去default page 
`HTTP/1.1` 代表我們使用的HTTP version為1.1
`Host: www.example.com`因為server 會可能回應其他多個網頁 
`...` 告訴server who you are 讓他們知道where to send
### 要求網址
![](https://i.imgur.com/sGhszkB.png)

### 想要求一個不存在的網址
用人類的話語來說
![](https://i.imgur.com/AwimZzJ.png)
電腦該如何溝通
![](https://i.imgur.com/nDZajS1.png)

## 常見的網頁回應
![](https://i.imgur.com/NiXpiFt.png)

### 自己嘗試去從network看
隨便查一個東西，跑200 ok
![](https://i.imgur.com/AU5oRD9.png)


打thefacebook(舊的名稱)會顯示302 ,301
![](https://i.imgur.com/yxtj6lu.png)

### 參考資料
[CS50 WEEK5-HTTP](https://cs50.harvard.edu/college/2018/fall/weeks/5/notes/)