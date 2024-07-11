# https://leetcode.com/problems/concatenation-of-array/
def getConcatenation(nums):
        result = []
        for i in range(2):
            for num in nums:
                result.append(num)
        return result
