# LeetCode Problem: 1518. Water Bottles
# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        while numBottles >= numExchange:  
            exchangedBottles = numBottles // numExchange  
            sum += exchangedBottles 
            numBottles = numBottles % numExchange + exchangedBottles  
        return sum
            