from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
两数相加
"""
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    temp = 0
    c = ListNode()
    e = c
    while l1 != None or l2 != None or temp > 0:
        val1 = l1.val if l1 != None else 0
        val2 = l2.val if l2 != None else 0
        total = val2 + val1 + temp
        temp = total // 10
        val3 = total % 10
        d = ListNode()
        d.val = val3
        e.next = d
        e = e.next
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    return c.next
"""
合并两个有序链表
"""
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    reslute=ListNode()
    Listreslute1=reslute
    while list1 !=None and list2 !=None:
        c = ListNode()
        if list1.val<=list2.val:
            c.val = list1.val
            list1=list1.next
        else:
            c.val = list2.val
            list2 = list2.next
        Listreslute1.next = c
        Listreslute1 = c
    Listreslute1.next=list1 if list1 !=None else list2
    return reslute.next

if __name__ == '__main__':
    a=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
    b=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
    print(mergeTwoLists(a,b))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
