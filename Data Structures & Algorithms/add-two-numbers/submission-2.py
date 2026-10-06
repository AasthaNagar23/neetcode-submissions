# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        curr=l1 
        while curr:
            a.append(str(curr.val))
            curr=curr.next
        curr1=l2
        while curr1:
            b.append(str(curr1.val))
            curr1=curr1.next
        num1=int("".join(a[::-1]))
        num2=int("".join(b[::-1]))
        res=str(num1+num2)
        ans=[]
        for i in res[::-1]:
            ans.append(int(i))
        head=ListNode(ans[0])
        curr=head
        for i in range(1,len(ans)):
            curr.next=ListNode(ans[i])
            curr=curr.next
        return head

        





