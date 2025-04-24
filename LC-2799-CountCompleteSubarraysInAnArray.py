# LeetCode Problem: 2799. Count Complete Subarrays In An Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/


def countCompleteSubarrays(nums):
    unique_elemets = []
    for num in nums:
        if num not in unique_elemets:
            unique_elemets.append(num)

    count_complete_subarrays = 0

    for start in range(len(nums)):
        element_frequency = {}

        for end in range(start, len(nums)):
            num = nums[end]
            if num not in element_frequency:
                element_frequency[num] = 1
            else:
                element_frequency[num] += 1

            if len(element_frequency) == len(unique_elemets):
                count_complete_subarrays += 1
    return count_complete_subarrays