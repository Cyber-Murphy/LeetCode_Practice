#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        r=0
        count=0
        while l<len(t) and r<len(s):
            if t[l]==s[r]:
                r+=1
                count+=1
            l+=1
        return count==len(s)
        
# @lc code=end

