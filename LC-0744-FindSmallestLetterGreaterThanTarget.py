# LeetCode Problem: 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if letters[mid] > target:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return letters[ans]
    

    # for i in range(len(letters)):
        #     if ord(letters[i]) > ord(target):
        #         return letters[i]
        
        # return letters[0]
