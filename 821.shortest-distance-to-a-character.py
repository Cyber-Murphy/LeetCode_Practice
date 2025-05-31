#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occur=[]
        result=[]
        for i in range(len(s)):
            if  s[i]==c:
                occur.append(i)
        for i in range(len(s)):
            min_occ=float('inf')
            for j in range(len(occur)):
                diff= abs(i-occur[j])
                min_occ=min(diff,min_occ)

            result.append(min_occ)
        return result
        


        
# @lc code=end

