# LeetCode Problem: 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        res = []

        for num in nums:
            total -= num
            res.append(abs(left_sum - total))
            left_sum += num

        return res


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_sum = [0] * n
        right_sum = [0] * n
        ans = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]

        for i in range(n):
            ans[i] = abs(left_sum[i] - right_sum[i])

        return ans