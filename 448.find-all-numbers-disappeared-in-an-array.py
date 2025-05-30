#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset=set()
        result=[]
        for i in nums:
            hashset.add(i)
        for i in range(1,len(nums)+1):
            if i not in hashset:
                result.append(i)

        return result

        
# @lc code=end

