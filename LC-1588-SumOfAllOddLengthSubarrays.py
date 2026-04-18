# LeetCode Problem: 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = []
        curr_total = 0
        for num in arr:
            curr_total += num
            prefix_sum.append(curr_total)

        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                if i == 0:
                    res += prefix_sum[j]
                else:
                    res += prefix_sum[j] - prefix_sum[i - 1]
        return res
    
    
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_of_subarray = 0
        n = len(arr)
        for length in range(1,n + 1, 2):
            for start in range(n - length + 1):
                for i in range(start, length + start):
                    sum_of_subarray += arr[i]
        return sum_of_subarray
