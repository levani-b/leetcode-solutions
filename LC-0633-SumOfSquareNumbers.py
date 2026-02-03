# LeetCode Problem: 633. Sum Of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0 , int(c ** 0.5)
        while l <= r:
            square_sum = (l * l) + (r * r)

            if square_sum == c:
                return True
            elif square_sum > c:
                r -= 1
            else:
                l += 1
        
        return False

