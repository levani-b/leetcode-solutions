# LeetCode Problem: 1470. Shuffle The Array
# https://leetcode.com/problems/shuffle-the-array/


def shuffle(nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
