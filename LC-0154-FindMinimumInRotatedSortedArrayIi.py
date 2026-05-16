# LeetCode Problem: 154. Find Minimum In Rotated Sorted Array Ii
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]