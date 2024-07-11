# https://leetcode.com/problems/remove-element/
def removeElement(nums, val):
    l = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l] = nums[i]
            l+=1
    return l
        