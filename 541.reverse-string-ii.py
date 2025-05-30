#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            l=i
            r=min(l+k-1,len(s)-1)
            while l<r:
                s[l],s[r]=s[r],s[l]
                r-=1
                l+=1
        return ''.join(s)
        
# @lc code=end

