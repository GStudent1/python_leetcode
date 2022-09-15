# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        list1_head = list1
        list2_head = list2
        list3_head = list3
        while list1_head and list2_head:
            if list1_head.val > list2_head.val:
                list_demo = ListNode()
                list3_head.next = list_demo
                list3_head = list3_head.next
                list3_head.val = list2_head.val
                list2_head = list2_head.next

            else:
                list_demo = ListNode()
                list3_head.next = list_demo
                list3_head = list3_head.next
                list3_head.val = list1_head.val
                list1_head=list1_head.next

        list3_head.next = list1_head if list1_head else list2_head
        return list3.next

    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        prehead = ListNode()
        prev = prehead
        while list1 and list2:
            if list1.val < list2.val:
                prev.next=list1
                prev=prev.next
                list1=list1.next
            else:
                prev.next = list2
                prev = prev.next
                list2 = list2.next
        prev.next=list1 if list1 else list2
        return prehead.next

if __name__ == '__main__':
    str1 = ListNode(1,ListNode(3,ListNode(5,ListNode(7))))
    str2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8,ListNode(9,ListNode(10))))))
    sol=Solution()
    list_print=sol.mergeTwoLists(str1,str2)
    while list_print:
        print(list_print.val)
        list_print=list_print.next