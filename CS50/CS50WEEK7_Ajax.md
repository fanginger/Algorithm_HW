

# CS50 WEEK7
> 想要更新網頁，但是不想要整個網頁重整只想要局部更新->足球分數，就可以使用Ajax
> 

## Ajax
>Asynchronous JavaScript and XML allows us to dynamically update a webpage even more dynamically.
>Ajax雖然名字是XML但是他只是名字，現在比較常用JSON
>

### 如何使用Ajax
使用JS object 的 `XMLHttpRequest`

```python
var xhttp = new XMLHttpRequest();
#create a new Http rquest

```

### onreadystatechange behavior 
A function that will descirbe the steps that are happening when you visit a page.簡單來說就是你現在的載入階段。
the readystate property will change from 0(request not yet initialized)to 1,2,3 and finally 4(request 已經結束reponse已經準備好)the status property will be 200(ok)


```javascript
function ajax_request(argument)
{
    var aj = new XMLHttpRequest();
    aj.onreadystatechange = function() {
        if(aj.readyState == 4 && aj.status == 200)
        //do someting to page
    };
    aj.open('GET','/*url*/',true);
    aj.send();
}
```

現在ajax的使用都常都是使用jquery居多，而非只是存粹的js