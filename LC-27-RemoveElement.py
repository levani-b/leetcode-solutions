# LeetCode Problem: 27. Remove Element
# https://leetcode.com/problems/remove-element/


def removeElement(nums, val):
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        return l