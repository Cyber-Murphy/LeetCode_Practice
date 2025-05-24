#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap={}
        nums=[]
        for string in arr:
            if string in hashmap:
                hashmap[string]+=1
            else:
                hashmap[string]=1
        for keys,value in hashmap.items():
            if value<2:
                nums.append(keys)
                
        if len(nums)>=k:
            return nums[k-1]
        else:
            return ""        
        
# @lc code=end

