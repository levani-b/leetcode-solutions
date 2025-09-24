# LeetCode Problem: 166. Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        result.append(str(numerator // denominator))
        numerator %= denominator
        
        if numerator == 0:
            return "".join(result)
        
        result.append(".")
        
        remainder_map = {}
        
        while numerator != 0:
            if numerator in remainder_map:
                cycle_start = remainder_map[numerator]
                result.insert(cycle_start, "(")
                result.append(")")
                break
            
            remainder_map[numerator] = len(result)
            
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator
        
        return "".join(result)