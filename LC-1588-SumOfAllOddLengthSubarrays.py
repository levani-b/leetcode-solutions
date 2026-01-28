# LeetCode Problem: 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_of_subarray = 0
        n = len(arr)
        for length in range(1,n + 1, 2):
            for start in range(n - length + 1):
                for i in range(start, length + start):
                    sum_of_subarray += arr[i]
        return sum_of_subarray
