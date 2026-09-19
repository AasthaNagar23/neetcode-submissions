# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = []
        curr = head
        while curr:
            a.append(curr)
            curr = curr.next
        left=0
        right=len(a)-1
        result=[]
        while left<=right:
            if left==right:
                result.append(a[left])
            else:
                result.append(a[left])
                result.append(a[right])
            left+=1
            right-=1
        for i in range(len(result)-1):
            result[i].next=result[i+1]
        result[-1].next=None
    
