#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        people.sort()
        if people[0]>=limit:
            return len(people)
        l=0
        r=len(people)-1
        while l<=r:
            if people[l]+people[r]<=limit:
                r-=1
                l+=1
                boat+=1
            else:
                boat+=1
                r-=1
        return boat
        
# @lc code=end

