#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1={}
        hash2={}
        result=[]
        for i in  range (len(nums1)):
            hash1[nums1[i]]=i
        for i in range(len(nums2)):
            hash2[nums2[i]]=i
        for key,value in hash1.items():
            if key in nums2:
                if key == max(nums2):
                    result.append(-1)
                    continue
                elif key==nums2[len(nums2)-1]:
                    result.append(-1)
                    continue
                for i in range(hash2[key]+1,len(nums2)):
                    if nums2[i]>key:
                        result.append(nums2[i])
                        break
                else:
                    result.append(-1)
                    
        return result



        



        


        
        
# @lc code=end

