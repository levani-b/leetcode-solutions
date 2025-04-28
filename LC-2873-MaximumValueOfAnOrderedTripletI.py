# LeetCode Problem: 2873. Maximum Value Of An Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

from typing import List

def maximumTripletValue(nums: List[int]) -> int:
        max = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    triplet_value = (nums[i] - nums[j]) * nums[k]
                    if triplet_value > max:
                        max = triplet_value
                    
        return max