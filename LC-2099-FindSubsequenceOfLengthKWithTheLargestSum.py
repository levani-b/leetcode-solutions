# LeetCode Problem: 2099. Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]

        top_k = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]

        top_k.sort(key=lambda x: x[1])
        
        return [num for num, _ in top_k]
