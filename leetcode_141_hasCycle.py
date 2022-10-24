"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
from typing import Optional


class ListNode:
     def __init__(self, x,next=None):
         self.val = x
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False


if __name__ == '__main__':
    str3=ListNode(-4)
    str2 = ListNode(2, ListNode(0,str3))
    str3.next=str2
    str1 = ListNode(3, str2)
    sol=Solution()
    print(sol.hasCycle(str2))