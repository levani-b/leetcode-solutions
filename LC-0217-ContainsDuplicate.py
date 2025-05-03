# LeetCode Problem: 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hashT = {}
    for num in nums:
        if num not in hashT:
            hashT[num] = 1
    
    if len(hashT) == len(nums):
        return False
    return True