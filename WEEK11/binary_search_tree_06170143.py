# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self,x):
#         self.val = x
#         self.left = None
#         self.right = None
#         """
#         :type val: int
#         :type left: TreeNode or None
#         :type right: TreeNode or None
#         """
# class Solution(object):
#     def insert(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode(inserted node)
#         """
#         # root 為node 
#         root = self.clean(root)
#         cur = root
#         node = TreeNode(val)
#         if cur.val:
#             while cur:
#                 if node.val > cur.val:
#                     if cur.right:
#                         cur = cur.right
#                     else:
#                         self.addAtright(cur,node)
#                         return node
#                 else:
#                     if cur.left:
#                         cur = cur.left
#                     else:
#                         self.addAtleft(cur,node)
#                         return node
#         root = node
#         return root
#         # node = TreeNode(val)
#         # cur = root
#         # if cur.val:
#         #     while cur:
#         #         if node.val > cur.val:
#         #             if cur.right:
#         #                 cur = cur.right
#         #             else:
#         #                 self.addAtright(cur,node)
#         #                 print(root)
#         #                 return root
#         #                 # FIXME:
#         #                 # return 新增的treenode
#         #         else:
#         #             if cur.left:
#         #                 cur = cur.left
#         #             else:
#         #                 self.addAtleft(cur,node)
#         #                 return root

#         # else:  
#         #     root.val = node.val
#         #     return root
            
#     def addAtright(self,head,node) -> None:
#         head.right = node

#     def addAtleft(self,head,node) -> None:
#         head.left = node
  
#     def delete(self, root, target):
#         """
#         :type root: TreeNode
#         :type target: int
#         :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
#         """
#     def search(self, root, target):
#         """
#         :type root: TreeNode
#         :type target: int
#         :rtype: TreeNode(searched node)
#         """
#         if root:
#             cur = root
#             while target != cur.val:
#                 if target > cur.val:
#                     if cur.right:
#                         cur = cur.right
#                     else:
#                         return None
#                 else:
#                     if cur.left:
#                         cur = cur.left
#                     else:
#                         return None
#             print(cur)
#             return cur
#         else:
#             return None
#     def modify(self, root, target, new_val):
#         """
#         :type root: TreeNode
#         :type target: int
#         :type new_val: int
#         :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
#         """
    
#     def print(self,root,mylist):
#         if root:
#             # print(root.val)
#             mylist.append(root.val)
#             self.print(root.left,mylist)
#             self.print(root.right,mylist)
#         # print(mylist)
#         return mylist

#     def printest(self,root):
#         if root:
#             print(root.val)

#             self.printest(root.left)

#             self.printest(root.right)

#     def clean(self,root):
#         mylist = []
#         self.print(root,mylist)
#         head = mylist[0]
#         mylist.pop(0)
#         node = TreeNode(head)
#         for i in mylist:
#             self.insertest(node,i)   
#         return node

#     def insertest(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode(inserted node)
#         """
#         # root 為node 
#         node = TreeNode(val)
#         cur = root
#         if cur.val:
#             while cur:
#                 if node.val > cur.val:
#                     if cur.right:
#                         cur = cur.right
#                     else:
#                         return self.addAtright(cur,node)
#                 else:
#                     if cur.left:
#                         cur = cur.left
#                     else:
#                         return self.addAtleft(cur,node)
#         root.val = node.val
#         return root

# sol = Solution()
# node1 = TreeNode(None)
# node2 = TreeNode(7)
# node3 = TreeNode(12)
# node4 = TreeNode(3)
# node5 = TreeNode(-5)
# node6 = TreeNode(10)
# node7 = TreeNode(9)

# # sol.insert(node1,1)
# sol.printest(node2)
# sol.insert(node2,1)
# print(sol.insert(node2,1)==node2.left)

# # node2.right = node3
# # # node3.left = node4
# # # node4.right = node5
# # # node2.left = node6
# # node2 = node2
# # node2 = sol.insert(node2,77)
# # # print(77 == node2.right.right.val)
# # # print(sol.insert(node2,77)==node2.right.right.val)
# # print()
# # find = sol.search(node2,77)

# # node2 = sol.insert(node2,77)
# # print( sol.insert(node2,77)== node2.right)


# # mylist = []
# # # sol.clean(node2)
# # # sol.print(node2,mylist)
# # node2 = sol.insert(node2,77)
# # sol.search(node2,77)
# # # FIXME:
# # # 這邊不會被記錄下來 就是node2 會是原本的node2 而非家了77的
# # node2 = sol.insert(node2,99)
# # sol.printest(node2)
# # # 7 12 3 -5 左10 
# # sol.printest(sol.clean(node2))

# # sol.insert(node1,12)
# # sol.insert(node1,3)
# # sol.insert(node1,1)
# # sol.search(node1,5)
# # sol.print(node1)

# # Definition for a binary tree node.
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
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if root ==  None: 
            return  None

        if target < root.val: 
            root.left = self.delete(root.left, target) 
    
        elif(target > root.val): 
            root.right = self.delete(root.right, target) 
    
        else: 
            if root.left == None and root.right == None:
                root = None
                return None
            elif root.left is None : 
                temp = root.right  
                root = None 
                return temp  
                
            elif root.right is None : 
                temp = root.left  
                root = None
                if self.search(temp,target) != None:
                    self.delete(temp,target)
                else:
                    return temp 
            else:
                # case 3
                temp = root
                while temp.right != None:
                    temp = temp.right
                #現在temp為最大的點，然後要把它刪掉
                
                root.val = temp.val
                self.deleteNode(root.right,temp.val)

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
            return 
        
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

sol = Solution()
node1 = TreeNode(None)
node2 = TreeNode(7)
node3 = TreeNode(12)
node4 = TreeNode(3)
node5 = TreeNode(-5)
node6 = TreeNode(10)
node7 = TreeNode(9)


node2.left = node3
node3.left = node4
node4.right = node5
node2.right = node6
sol.insert(node2,5)
print(sol.insert(node2,55)==node2.right.right)
# print(sol.search(node2,55)==node2.right.right)
# sol.search(node2,55)
sol.modify(node2,5,77)
# sol.search()
# sol.clean(node2)
sol.printest(node2)

# node2 = sol.insert(node2,77)
# # print(77 == node2.right.right.val)
# # print(sol.insert(node2,77)==node2.right.right.val)
