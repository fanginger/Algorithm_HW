class Solution:
   
    def sortList(self,mylist,front,end):
        #這邊就是丟進去會開始區分
        if front<end:
            pivot = self.partition(mylist,front,end)
            #區分兩堆 
            self.sortList(mylist,front,pivot-1)
            self.sortList(mylist,pivot+1,end)
        return mylist
    def partition(self,mylist,front,end):
        i = front-1
        j = front
        pivot = mylist[end]
        while j < end:
            #mylist[j] != pivot
            if(mylist[j]>pivot):
                j +=1
            else:
                # (mylist[j]<=pivot)
                i+= 1
                mylist[j],mylist[i] = mylist[i],mylist[j]
                j+=1
        i+=1
        # j+=1
        mylist[j],mylist[i] = mylist[i],mylist[j]
        return i 
    

list_test = [2,3,8,3,1,22,83,33,5,9,1]
sol = Solution()

ans = sol.sortList(list_test , 0 ,len(list_test)-1)

print(ans)

list_test2 = [62,32,1,3,5,34,653,4,2,1,34,54,3,1]
sol2 = Solution()

ans2 = sol2.sortList(list_test2 , 0 ,len(list_test2)-1)

print(ans2)