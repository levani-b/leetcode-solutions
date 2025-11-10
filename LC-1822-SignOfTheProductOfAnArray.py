# LeetCode Problem: 1822. Sign of the product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                0
        
        product = 1
        for num in nums:
            product *= num
        
        res = signFunc(product)
        return res