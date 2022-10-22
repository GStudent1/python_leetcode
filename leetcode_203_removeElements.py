from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        New_Head=ListNode()
        New_Head.next=head
        newhead=New_Head
        if head==None:
            return head
        while newhead.next is not None:
            if newhead.next.val==val:
                if newhead.next.next is not None:
                    newhead.next=newhead.next.next
                else:
                    newhead.next = None
            else:
                newhead=newhead.next
        return New_Head.next
if __name__ == '__main__':
    str1 = ListNode(1,ListNode(3,ListNode(5,ListNode(7))))
    #str2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8,ListNode(9,ListNode(10))))))
    sol=Solution()
    list_print=sol.removeElements(str1,3)
    while list_print:
        print(list_print.val)
        list_print=list_print.next



