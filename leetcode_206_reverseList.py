from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=None
        newhead=head
        if newhead==None:
            return head
        while newhead !=None:
            temp=newhead.next
            newhead.next=result
            result=newhead
            newhead=temp
        return result


if __name__ == '__main__':
    #str1 = ListNode(1,ListNode(3,ListNode(5,ListNode(7))))
    str2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8,ListNode(9,ListNode(10))))))
    sol=Solution()
    list_print=sol.reverseList(str2)
    while list_print:
        print(list_print.val)
        list_print=list_print.next



