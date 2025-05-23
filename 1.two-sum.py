#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmaps={}
      for i in range(len(nums)):
         complement=target-nums[i]
         if complement in hashmaps:
            return [hashmaps[complement],i]
         hashmaps[nums[i]]=i
# @lc code=end

