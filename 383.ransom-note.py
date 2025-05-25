#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1={}
        hash2={}
        for i in ransomNote:
            if i in hash1:
                hash1[i]+=1
            else:
                hash1[i]=1
        for i in magazine:
            if i in hash2:
                hash2[i]+=1
            else:
                hash2[i]=1
        for key,value in hash1.items():
            if key not in hash2 or hash1[key]>hash2[key]:
                return False
        return True
        
            
                
        
        



        
# @lc code=end

