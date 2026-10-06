# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for head in lists:
            current=head
            while current:
                arr.append(current.val)
                current=current.next
        arr.sort()
        if not arr:
            return None
        head=ListNode(arr[0])
        curr=head
        for i in range(1,len(arr)):
            curr.next=ListNode(arr[i])
            curr=curr.next

        return head