# LeetCode Problem: 2364. Count Number Of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        all_pairs = (n * (n - 1)) // 2
        
        hashmap = {}
        good_pairs = 0
        
        for i in range(len(nums)):
            diff = nums[i] - i
            
            if diff in hashmap:
                good_pairs += hashmap[diff]
            
            hashmap[diff] = hashmap.get(diff, 0) + 1
        
        bad_pairs = all_pairs - good_pairs
        return bad_pairs