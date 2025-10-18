# LeetCode Problem: 2206. Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num, count in freq.items():
            if count % 2 == 1:
                return False
        return True