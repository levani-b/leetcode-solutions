# LeetCode Problem: 1431. Kids With The Greatest Number Of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    res = []
    max = 0
    for candy in candies:
        if candy > max:
            max = candy
    
    for candy in candies:
        if candy + extraCandies >= max:
            res.append(True)
        else:
            res.append(False)
    return res