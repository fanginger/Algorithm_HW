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


list_test = [2,3,8]
# sol = Solution()

ans = Solution().merge_sort(list_test )

print(ans)

