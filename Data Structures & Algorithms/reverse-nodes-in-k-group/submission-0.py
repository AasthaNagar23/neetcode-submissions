# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        if not head:
            return None
        curr=head
        while curr:
            arr.append(curr)
            curr=curr.next
        for i in range(0,len(arr)-k+1,k):
            arr[i:i+k]=arr[i:i+k][::-1]
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[0]