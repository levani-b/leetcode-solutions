# LeetCode Problem: 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        balls = 0
        moves = 0
        for i in range(len(boxes)):
            answer[i] = balls + moves
            moves += balls
            balls += int(boxes[i])

        balls = 0
        moves = 0
        for i in range(len(boxes) - 1, -1, -1):
            answer[i] += balls + moves
            moves += balls
            balls += int(boxes[i])
        
        return answer