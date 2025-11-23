# LeetCode Problem: 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]
        stack = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            
            if stack:
                answer[i] = prices[i] - prices[stack[-1]]
            
            stack.append(i)
        
        return answer