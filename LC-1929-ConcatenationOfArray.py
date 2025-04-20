# LeetCode Problem: 1929. Concatenation Of Array
# https://leetcode.com/problems/concatenation-of-array/

def getConcatenation(nums):
        result = []
        for _ in range(2):
            for num in nums:
                result.append(num)
        return result