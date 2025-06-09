# LeetCode Problem: 121. Best Time To Buy And Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price

            if price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit