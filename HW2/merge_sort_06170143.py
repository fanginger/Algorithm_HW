class Solution(object):
    def merge_sort(self, mylist):
        if len(mylist) == 1:
            return mylist
        else:
            left = self.merge_sort(mylist[0:(len(mylist)//2)])
            right = self.merge_sort(mylist[(len(mylist)//2):])
            newlist = self.merge(left,right)
            return newlist
    def merge(self,left,right):
        temp = []
        a = right[0]
        b = left[0]
        while len(right) != 0 and len(left) !=0:
            a = right[0]
            b = left[0]
            if a<b:
                temp.append(a)
                right.pop(0)
            else:
                temp.append(b)
                left.pop(0)
        temp.extend(left)       
        temp.extend(right)
        return temp 



class Solution2(object):
    def heap_sort(self, mylist):
        end = []
        while len(mylist)>0:
            for i in range((len(mylist)//2),0,-1):
                self.heapify(mylist,i)
            end.append(mylist[0])
            mylist.pop(0)   
        return end
    def heapify(self,mylist,endpoint):
        if(endpoint == 1):
            parent = 0
        else:
            parent = endpoint//2+1
        left = endpoint*2-1
        right = endpoint*2

        if(mylist[left] < mylist[parent]):
            
            mylist[left],mylist[parent] =  mylist[parent],mylist[left]
        if(right> len(mylist)-1):
            return

        if( mylist[right] < mylist[parent]):
            
            mylist[right],mylist[parent] =  mylist[parent],mylist[right]

 



import random
import numpy as np
x = np.random.randint(1,1000,10000)
#隨機生成數字
list_test = x.tolist()

#轉換成list
# list_test = [8,2,3,1,2,2,7,4,2,-1,33,22,100]
# sol = Solution()


#list_test = [8,2,3,1,2,2,7,4,2,-1,33,22,100]
# sol = Solution()

ans = Solution().merge_sort(list_test)
print(ans)

