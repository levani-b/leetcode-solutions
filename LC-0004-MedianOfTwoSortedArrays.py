# LeetCode Problem: 4. Median Of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                nums.append(nums2[r])
                r += 1
            else:
                nums.append(nums1[l])
                l += 1
        nums += nums1[l:]
        nums += nums2[r:]
        
        mid = len(nums)//2
        n = len(nums)
        
        if n % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1])/2
