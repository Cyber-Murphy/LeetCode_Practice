#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        storeUniqueNumber=set()
        while n>0:
            sumofsquare=0
            for i in str(n):
                sumofsquare+=int(i)*int(i)
            if sumofsquare==1:
                return True
            if sumofsquare in storeUniqueNumber:
                return False
            storeUniqueNumber.add(sumofsquare)
            n=sumofsquare
            
            

        
# @lc code=end

