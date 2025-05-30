#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        start=0
        s=list(s)
        for i in range(len(s)):
            if i==len(s)-1 or s[i]==' ' :
                l=start
                r= i-1 if s[i]==' ' else i
                while l<r:
                    s[i],s[r]=s[r],s[l]

                start=i
        return ''.join(s)

        
# @lc code=end

