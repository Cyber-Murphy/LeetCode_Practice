#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]%2==0:
                l+=1
            elif nums[r]%2!=0:
                r-=1
            elif nums[l]%2!=0 and nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
        return nums
      
        

    
        
         
          

# @lc code=end

