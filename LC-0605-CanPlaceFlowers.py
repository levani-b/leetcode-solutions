# LeetCode Problem: 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                if i == 0:
                    empty_left = True
                else:
                    if flowerbed[i-1] == 0:
                        empty_left == True
                    else:
                        empty_left == False

                if i == length - 1:
                    empty_right = True
                else:
                    if flowerbed[i + 1] == 0:
                        empty_right = True
                    else:
                        empty_right = False

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
