# LeetCode Problem: 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in range(len(accounts)):
            customer_money = 0
            for j in range(len(accounts[i])):
                customer_money += accounts[i][j]
            if customer_money > maximum:
                maximum = customer_money
        
        return maximum