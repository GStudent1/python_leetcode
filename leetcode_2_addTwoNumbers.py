"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers1(self,l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        temp=result
        carry=0
        while l1 !=None or l2 !=None or carry>0:
            l1val=l1.val if l1!=None else 0
            l1va2 = l2.val if l2 != None else 0
            sum=l1val+l1va2+carry
            carry=sum // 10
            curr=sum % 10
            currnode = ListNode()
            currnode.val=curr
            temp.next=currnode
            temp=temp.next
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None

        return result.next


if __name__ == '__main__':

    nums = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
    target = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
    sol=Solution()
    ln=sol.addTwoNumbers1(nums, target)
    lnn=ln
    while ln:
        print(ln.val)
        ln=ln.next


