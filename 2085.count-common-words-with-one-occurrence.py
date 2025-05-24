#
# @lc app=leetcode id=2085 lang=python3
#
# [2085] Count Common Words With One Occurrence
#

# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hashmap1={}
        hashmap2={}
        for i in words1:
            if i in hashmap1:
               hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for i in words2:
            if i in hashmap2:
                hashmap2[i]+=1
            else:
                hashmap2[i]=1
        count=0
        for key,value in hashmap1.items():
            if key in hashmap2:
                if hashmap1[key]==1 and hashmap2[key]==1:
                    count+=1
        return count
        





        
# @lc code=end

