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
        # root 為node 
        # self.root = root
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

            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
                
            if root.right is None : 
                temp = root.left  
                root = None
                return temp 
    
            else:
                temp = root.left
                while root.left:
                    temp = temp.left
       
                root.val = temp.val 

                root.right = self.delete_2(root.right , temp.val) 

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
            # print(root.val)
            mylist.append(root.val)
            self.print(root.left,mylist)
            self.print(root.right,mylist)
        # print(mylist)
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