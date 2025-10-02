# LeetCode Problem: 3100. Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
    
        while  empty >= numExchange:
            empty -= numExchange
            total += 1
            numExchange += 1
            empty += 1
        
        return total