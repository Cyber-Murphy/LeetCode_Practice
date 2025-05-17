#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unqiue= set()
        for i in range(len(nums)):
            if nums[i] not in unqiue:
                unqiue.add(nums[i])

        unqiue_list = list(unqiue)
        for i in range(len(unqiue)):
            nums[i]=unqiue_list[i]
        return len(unqiue)
        
# @lc code=end

