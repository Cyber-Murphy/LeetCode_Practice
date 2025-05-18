#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxsum=nums[0]
        for i in range(len(nums)):
            cursum= max(cursum,0)
            cursum+=nums[i]
            maxsum=max(maxsum,cursum)
        return maxsum
        
# @lc code=end

