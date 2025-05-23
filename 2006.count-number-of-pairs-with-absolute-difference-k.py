#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        hashmap={}
        for num in nums:
            if num-k in hashmap:
                count= count+ hashmap[num-k]
            if num+k in hashmap:
                count +=hashmap[num+k]
            
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        return count
        
# @lc code=end

