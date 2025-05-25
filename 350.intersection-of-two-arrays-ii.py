#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1={}
        hash2={}
        for i in nums1:
            if i in hash1:
                hash1[i]+=1
            else:
                hash1[i]=1
        for i in nums2:
            if i in hash2:
                hash2[i]+=1
            else:
                hash2[i]=1
        result=[]
        for key,value in hash1.items():
            if key in hash2:
                result+= [key]*min(hash1[key],hash2[key])
        return result



        
# @lc code=end

