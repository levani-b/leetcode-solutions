# LeetCode Problem: 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            found = False
            next_greater = -1
            
            for j in range(len(nums2)):
                if num == nums2[j]:
                    found = True
                elif found and nums2[j] > num:
                    next_greater = nums2[j]
                    break
            res.append(next_greater)
        return res