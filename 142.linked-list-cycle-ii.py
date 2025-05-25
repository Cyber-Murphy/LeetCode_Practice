#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        temp=head
        if head is None:
            return None
        if head.next is None:
            return None 
        while fast and fast.next:
            fast=fast.next.next 
            slow=slow.next 
            if fast==slow:
                while temp!=fast:
                    fast=fast.next 
                    temp=temp.next
                return temp
        return None
                
        
# @lc code=end

