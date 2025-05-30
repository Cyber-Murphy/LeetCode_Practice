#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        l=m-1
        r=n-1
        last=m+n-1
        while r>=0:
            if l>=0 and nums1[l]>=nums2[r]:
                nums1[last]=nums1[l]
                l-=1
            else:
                nums1[last]=nums2[r]
                r-=1
            last-=1
        
# @lc code=end

