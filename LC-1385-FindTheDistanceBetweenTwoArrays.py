# LeetCode Problem: 1385. Find The Distance Between Two Arrays
# https://leetcode.com/problems/find-the-distance-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = len(arr1)
        arr2.sort()
        for num in arr1:
            lo = 0
            hi = len(arr2) - 1

            while lo <= hi:
                mid = (lo + hi) // 2

                if arr2[mid] < num - d:
                    lo = mid + 1
                elif arr2[mid] > num + d:
                    hi = mid - 1
                else:
                    count -= 1
                    break

        return count
