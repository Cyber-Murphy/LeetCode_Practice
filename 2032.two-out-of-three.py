#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        hashmap={}
        for num in nums1:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for num in nums2:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for num in nums3:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        result=[]
        for keys,value in hashmap.items():
            if value>=2:
                result.append(keys)
        return result



        
# @lc code=end

