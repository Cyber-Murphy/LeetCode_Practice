#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result=[]
        temp=head
        while temp:
            result.append(temp.val)
            temp=temp.next
        l=0
        r=len(result)-1
        while l<r:
            if result[l]!=result[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        
# @lc code=end

