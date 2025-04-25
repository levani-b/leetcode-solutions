# LeetCode Problem: 2656. Maximum Sum With Exactly K Elements
# https://leetcode.com/problems/maximum-sum-with-exactly-K-elements/

def maximizeSum(nums, k):
        nums.sort()
        sum = 0
        for _ in range(k):
            sum += nums[-1]
            nums[-1] += 1
        return sum