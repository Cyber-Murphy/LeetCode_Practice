#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(3)
        tail=dummy
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val>=temp2.val:
                tail.next=temp2
                temp2=temp2.next 
            else:
                tail.next=temp1
                temp1=temp1.next 
            tail=tail.next 
        if temp1:
            tail.next =temp1
        else:
            tail.next =temp2
        return dummy.next


        
# @lc code=end

