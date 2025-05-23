#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
        if count==n:
            return head.next 
        temp=head
        for i in range(count-n-1):
            temp=temp.next 
        temp.next=temp.next.next
        return head
        
# @lc code=end

