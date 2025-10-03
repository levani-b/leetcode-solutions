# LeetCode Problem: 3697. Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        exponent = 0

        while n > 0:
            remain = n % 10
            n //= 10
            if remain == 0:
                pass
            else:
                res.append(remain * 10**exponent)
            exponent += 1
            
        return res[::-1]