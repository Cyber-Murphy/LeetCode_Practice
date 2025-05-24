#
# @lc app=leetcode id=2068 lang=python3
#
# [2068] Check Whether Two Strings are Almost Equivalent
#

# @lc code=start
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hashmap1={}
        hashmap2={}
        for i in word1:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for i in word2:
            if i in hashmap2:
                hashmap2[i]+=1
            else:
                hashmap2[i]=1
        #So this is comparing hashmap1 to hashmap2
        for key,value in hashmap1.items():
            if key in hashmap2:
                count= abs(hashmap1[key]-hashmap2[key])
                if count>3:
                    return False
            elif value>3:
                return False
        #this will compare hashmap2 to hashmap1
        for key,value in hashmap2.items():
            if key not in hashmap1 and value>3:
                return False
        return True 

        
# @lc code=end

