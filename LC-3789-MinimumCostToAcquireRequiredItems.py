# LeetCode Problem: 3789. Minimum Cost To Acquire Required Items
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 == 0 and need2 == 0:
            return 0

        both = min(need1, need2)

        op1 = (cost1 * need1) + (cost2 * need2)
        op2 = max(need1, need2) * costBoth
        op3 = (
            (both * costBoth)
            + (need1 - both) * cost1
            + (need2 - both) * cost2
        )

        return min(op1, op2, op3)
