# LeetCode Problem: 1716. Calculate Money In Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        total = 0
        week = 0
        while day < n:
            if day % 7 == 0:
                week += 1
            day_of_week = day % 7
            total += week + day_of_week
            day += 1
        return total
