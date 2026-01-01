# LeetCode Problem: 2110. Number Of Smooth Descent Periods Of A Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        length = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                length += 1
            else:
                length = 1

            count += length
        return count + 1