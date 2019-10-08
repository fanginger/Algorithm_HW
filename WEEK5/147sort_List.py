# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

  
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         out = head
#         head = head.next
#         tail = out
#         while head:
#             temp = head
#             head = head.next
#             if temp.val <= out.val:
#                 temp.next = out
#                 out = temp
#             elif temp.val >= tail.val:
#                 tail.next = temp
#                 tail = temp
#             else:
#                 it = out
#                 while it.next != tail and it.next.val < temp.val:
#                     it = it.next
#                 temp.next = it.next
#                 it.next = temp
#         tail.next = None
#         return out
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        start = head
        
        while start:
            #外圈
            if start.next == None:
                break

            cur = start.next 

            while cur:
                #內圈
               
                if start.val > cur.val:
                    start.val,cur.val = cur.val,start.val
                   

                cur = cur.next
        
            start = start.next
        return head