# LeetCode Problem: 2833. Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq = {}
        for move in moves:
            if move in freq:
                freq[move] += 1
            else:
                freq[move] = 1
        
        R = freq.get('R', 0)
        L = freq.get('L', 0)
        blank = freq.get('_', 0)

        return abs(R - L) + blank