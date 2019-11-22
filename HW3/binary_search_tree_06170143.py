class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """

        self.clean(root)
        return self.insertest(root,val)

    def addAtright(self,head,node) -> None:
        head.right = node

    def addAtleft(self,head,node) -> None:
        head.left = node
    def search(self,root,target):
        root = self.clean(root)
        if root:
            cur = root
            while target != cur.val:
                if target > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        return None
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        return None
            print(cur)
            return cur
        else:
            return None
    def delete(self,root,target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete_2 nodes(maybe more than more) instead.(cannot search())
        """
        while self.search(root,target):
            self.delete_2(root,target)
        return root
    def delete_2(self, root, target):
        if root is None: 
            return root  
  
        if target < root.val: 
            root.left = self.delete_2(root.left,target) 

        elif(target > root.val): 
            root.right = self.delete_2(root.right, target) 
    
        else:  
            if root.left == None and root.right == None:
                root = None
                return None

            if root.left == None : 
                return root.right  
                
            if root.right == None : 
                return root.left  
    
            else:
                temp = root.left
                while temp.right:
                    temp = temp.right
       
                root.val = temp.val 

                root.left = self.delete_2(root.left , temp.val)

                return root 
        return root  
    
    
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """

        if self.search(root,target) == None:
            return None
        else:
            self.clean(root)
            while self.search(root,target):
                self.search(root,target).val = new_val
                self.clean(root)
            return root
        
    def print(self,root,mylist):
        if root:
            mylist.append(root.val)
            self.print(root.left,mylist)
            self.print(root.right,mylist)
        return  mylist

    def printest(self,root):
        if root:
            print(root.val)

            self.printest(root.left)

            self.printest(root.right)

    def clean(self,root):
        
        mylist = []
        self.print(root,mylist)
        head = mylist[0]
        mylist.pop(0)
        nodetemp = TreeNode(head)
        for i in mylist:
            self.insertest(nodetemp,i)  
        root.val = nodetemp.val
        root.right = nodetemp.right
        root.left = nodetemp.left
        return root
        

    def insertest(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        node = TreeNode(val)
        cur = root
        if cur.val:
            while cur:
                if node.val > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        self.addAtright(cur,node)
                        return node
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        self.addAtleft(cur,node)
                        return node
        root.val = node.val
        return root

"""
參考資料

[Tree系列文章](http://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)他整理的真的很好，看了一下delete的觀念(因為我不是很懂)
[Binary Search Tree | Set 2 (Delete)](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/) 看了他的delete 因為在寫case3時會遇到問題，所後看了一下，還是跟遞迴是有關聯的。所以之後可能再次複習遞迴或是多加練習。
[youtube影片](https://www.youtube.com/watch?v=pYT9F8_LFTM)再次建立delete觀念
與朋友討論整理這部分要怎麼寫，討論時間約10分鐘。最後他提醒我要用pointer的想法，因為我那時候就是想說可以使用等號就可以把整顆樹複製過去，但是這樣會產生一個問題，就是我是建立一顆新的樹。所以他給我的建議是要用pointer。無程式碼上面的實質幫助。
[pointer的概念](https://michaelchen.tech/c-programming/pointer/)

"""