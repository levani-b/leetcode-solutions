# LeetCode Problem: 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            heaviest = stones[0]
            second = stones[1]
            
            stones.pop(0)
            stones.pop(0)
            
            if heaviest != second:
                stones.append(heaviest - second)

        return stones[0] if stones else 0
        