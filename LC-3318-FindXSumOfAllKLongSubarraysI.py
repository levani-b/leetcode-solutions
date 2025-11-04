# LeetCode Problem: 3318. Find X-Sum Of All K-Long Subarrays I
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(numbers):
            freq = {}
            for num in numbers:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            
            if len(freq) <= x:
                return sum(numbers)

            sorted_items = sorted(freq.items(), key=lambda item: (item[1], item[0]),reverse=True)

            x_sum = 0
            for i in range(min(x, len(sorted_items))):
                value, frequency = sorted_items[i]
                x_sum += value * frequency
            
            return x_sum
        
        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            window = nums[i: i + k]
            xsum = x_sum(window)
            answer.append(xsum)
        
        return answer