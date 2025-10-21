# LeetCode Problem: 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            left_empty, right_empty = False, False
            if i == 0 or flowerbed[i - 1] == 0:
                left_empty = True

            if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                right_empty = True

            if left_empty and flowerbed[i] == 0 and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
