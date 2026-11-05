# LeetCode Problem: 2461. Maximum Sum Of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        curr_sum = sum(nums[:k])

        for num in nums[:k]:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_sum = 0
        if len(freq) == k:
            max_sum = curr_sum

        for i in range(k, len(nums)):
            old = nums[i - k]
            new = nums[i]

            curr_sum -= old
            freq[old] -= 1

            if freq[old] == 0:
                del freq[old]

            curr_sum += new

            if new in freq:
                freq[new] += 1
            else:
                freq[new] = 1

            if len(freq) == k:
                max_sum = max(curr_sum, max_sum)

        return max_sum
