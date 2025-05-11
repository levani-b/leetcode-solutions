# LeetCode Problem: 1550. Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

from typing import List


def threeConsecutiveOdds(arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if num % 2 == 1:
                odd_count +=1
                if odd_count == 3:
                    return True
            else:
                odd_count = 0
        return False