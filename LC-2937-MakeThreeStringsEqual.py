# LeetCode Problem: 2937. Make Three Strings Equal
# https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ops = 0
        while not (s1 == s2 == s3):
            max_len = max(len(s1), len(s2), len(s3))
            if len(s1) == max_len:
                if len(s1) == 1:
                    return -1
                s1 = s1[:-1]
                ops += 1
            elif len(s2) == max_len:
                if len(s2) == 1:
                    return -1
                s2 = s2[:-1]
                ops += 1
            else:
                if len(s3) == 1:
                    return -1
                s3 = s3[:-1]
                ops += 1
        return ops