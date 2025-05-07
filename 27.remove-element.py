#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                stack.append(nums[i])
        
        for i in range(len(stack)):
            nums[i]=stack[i]
        return len(stack)
        
# @lc code=end
