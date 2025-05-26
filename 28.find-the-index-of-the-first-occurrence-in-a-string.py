#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j+=1
            if j==m:
                return i
        return -1
        
# @lc code=end


