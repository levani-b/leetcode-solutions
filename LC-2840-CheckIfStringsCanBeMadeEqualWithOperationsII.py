# LeetCode Problem: 2840. Check if Strings Can be Made Equal With Operations Ii
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = sorted(s1[i] for i in range(0, len(s1), 2))
        even2 = sorted(s2[i] for i in range(0, len(s2), 2))

        odd1  = sorted(s1[i] for i in range(1, len(s1), 2))
        odd2  = sorted(s2[i] for i in range(1, len(s2), 2))

        return even1 == even2 and odd1 == odd2