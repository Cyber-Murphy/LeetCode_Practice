#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap={}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in t:
            if i in hashmap:
                hashmap[i]-=1
                if hashmap[i]<0:
                    return i
            else:
                return i
        return ""
        
# @lc code=end

