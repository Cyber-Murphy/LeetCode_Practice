#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x=str(x)
        l=0
        r=len(x)-1
        while l<r:
            if x[l]!=x[r]:
                return False
            l+=1
            r-=1
        return True
        
# @lc code=end

