# LeetCode Problem: 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(len(prices) - 1):
            curr_profit = 0
            if prices[i] < prices[i + 1]:
                curr_profit = prices[i + 1] - prices[i]
            
            total_profit += curr_profit

        return total_profit