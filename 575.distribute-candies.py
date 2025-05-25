#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies={}
        n=len(candyType)
        for i in candyType:
            if i in candies:
                candies[i]+=1
            else:
                candies[i]=1
        return min(len(candies),n//2)
        
# @lc code=end

