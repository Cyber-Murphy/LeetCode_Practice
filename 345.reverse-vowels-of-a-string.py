#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        #this i am solving via set
        vowels=set('aeiouAEIOU')
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] in vowels and s[r] not in vowels:
                r-=1
            elif s[l] not in vowels and s[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(s)
        
# @lc code=end

