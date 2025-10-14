# LeetCode Problem: 3712. Sum Of Elements With Frequency Divisible By K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sum = 0

        for num, count in freq.items():
            if count % k == 0:
                sum += num * count
            
        return sum