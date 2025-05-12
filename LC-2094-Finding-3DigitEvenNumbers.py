# LeetCode Problem: 2094. Finding 3 Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

from typing import List


def findEvenNumbers(digits: List[int]) -> List[int]:
        digits.sort()
        n = len(digits)

        ans = set()
        for i in range(n):
            if digits[i] != 0:
                for j in range(n):
                    if i != j:
                        for k in range(n):
                            if i != k and j != k and digits[k] % 2 == 0:
                                ans.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return sorted(list(ans))