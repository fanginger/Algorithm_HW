# conda
## 簡單介紹
>Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. It was created for Python programs, but it can package and distribute software for any language.
>


## 一定有的疑問(What is the difference between pip and conda?)


![](https://i.imgur.com/ErhoVKM.png)


 >之前我根本不知道可以用`conda install`然後我一直使用`pip install`我也搞不清楚到底幹嘛要用`conda`都已經有
`pip`

網友回答：簡單來說兩者就是不同的形式。但是你在使用時不可以互相交換著用。~~就是你想下載某一個套件使用的是conda 下一個就是pip。~~ 這我自己舉的還要問問看
但是他們不會互相影響對方。
![](https://i.imgur.com/iUb73a9.png)

anaconda自己寫一篇關於比較兩者[Understanding Conda and Pip](https://www.anaconda.com/understanding-conda-and-pip/)

其中提到幾點
1. pip只限用python conda 還可以與C或是R
2. conda 可以開虛擬環境pip不行


![](https://i.imgur.com/4l7u0nF.png)

## conda基本指令

- `conda --version`目前conda版本
- `conda install PACKAGE`下載套件
- `conda remove PACKAGE`刪除套件
- `conda list`看目前有的套件
- `conda create --name ENVIRONMENT python=MAIN.MINOR.PATCH`建立新環境
- `conda list --ENVIROMENT`檢視指定工作環境安裝的套件清單
- `conda activate ENVIRONMENT`切換到某個環境
- `conda deactivate`回到bash環境
- `conda remove --name ENVIRONMENT --all`刪除某環境

### 下載時遇到一個問題_PackagesNotFoundError: The following packages are not available from current channels
前幾天我在下載一個套件以為很簡單殊不知我一直遇到麻煩可能是第一次下載遇到這種事情
> 大部分要下載的套件都可以在預設的channel下載到，但是我那天要下載的剛好就不是。所以網上說要去另一個channel來下載像是conda-forge，然後打conda install --channel ORGANIZATION PACKAGE_NAME 就可以

1. 進入 https://anaconda.org/
2. 打入你要的套件

![](https://i.imgur.com/ppQQr1L.png)

3. 點擊一個下載方法


![](https://i.imgur.com/gkp5EvR.png)

4. 終於成功啦><
>有沒有注意到channel為forge?!!


### 參考資料
[What is the difference between pip and conda?](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda)
[輕鬆學習 Python：conda 的核心功能](https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025)