# LeetCode Problem: 1524. Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even_count = 1
        odd_count = 0
        curr_sum = 0
        count = 0

        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 1:
                count += even_count
                odd_count += 1
            else:
                count += odd_count
                even_count += 1
        
        return count % (10**9 + 7)
            
