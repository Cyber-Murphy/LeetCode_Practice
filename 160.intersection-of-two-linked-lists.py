#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1=headA
        temp2=headB
        while temp1!=temp2:
            if temp1 is None:
                temp1=headB
            else:
                temp1=temp1.next 
            if temp2 is None:
                temp2=headA
            else:
                temp2=temp2.next 
        return temp1
        
# @lc code=end

