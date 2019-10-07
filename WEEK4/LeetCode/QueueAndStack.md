# Queue And Stacks

Queue是具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。

如同普遍認知的排隊隊伍，Queue也具有以下特徵：

隊伍有前方(以front表示)以及後方(以back表示)之分。
若要進入隊伍(Push)，一定是從back進入。
若要離開隊伍(Pop)，一定是從front離開。
以圖一為例，由front(隊伍前方)和back(隊伍後方)可以判斷，進入隊伍的順序應該是23、1、3、35。

![](https://i.imgur.com/mJlbCxw.png)