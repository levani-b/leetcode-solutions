# LeetCode Problem: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curr_sum = sum(arr[:k])
        
        if curr_sum >= threshold * k:
                count += 1

        for i in range(k, len(arr)):
            curr_sum = curr_sum - arr[i - k] + arr[i]
            if curr_sum >= threshold * k:
                count += 1

        return count