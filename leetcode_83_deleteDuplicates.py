from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        if head is None:
            return node
        while head.next:
            if head.val == (head.next).val:
                head.next=(head.next).next
            else:
                head=head.next
        return node


if __name__ == '__main__':
    str1 = ListNode(1,ListNode(1,ListNode(5,ListNode(7,ListNode(7,ListNode(7))))))
    sol=Solution()
    list_print=sol.deleteDuplicates(str1)
    while list_print:
        print(list_print.val)
        list_print=list_print.next