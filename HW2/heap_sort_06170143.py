
class Solution(object):
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

 

