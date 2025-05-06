# LeetCode Problem: 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
        consecutive_ones = []
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                consecutive_ones.append(count)
                count = 0
        consecutive_ones.append(count)

        max = 0
        for max_n in consecutive_ones:
            if max_n > max:
                max = max_n
        return max



# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         curr_count = 0
#         max_count = 0

#         for num in nums:
#             if num == 1:
#                 curr_count += 1
#                 max_count = max(curr_count, max_count)
#             else:
#                 curr_count = 0
#         return max_count