#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprofit=float('inf')
        for i in prices:
            minprofit=min(minprofit,i)
            profit=i-minprofit
            maxprofit=max(maxprofit,profit)
        return maxprofit
        
# @lc code=end

