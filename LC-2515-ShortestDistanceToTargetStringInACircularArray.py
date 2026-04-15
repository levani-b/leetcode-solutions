# LeetCode Problem: 2515. Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        n = len(words)
        shortest_distance = float('inf')
        
        for i in range(n):
            if words[i] == target:
                forward = abs(startIndex - i)
                backward = n - forward
                shortest_distance = min(shortest_distance, forward, backward)
        
        return shortest_distance