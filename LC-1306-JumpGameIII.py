# LeetCode Problem: 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/

from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])
        n = len(arr)
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True

            forward = i + arr[i]
            if forward < n and forward not in visited:
                visited.add(forward)
                queue.append(forward)

            backward = i - arr[i]
            if backward >= 0 and backward not in visited:
                visited.add(backward)
                queue.append(backward)

        return False


