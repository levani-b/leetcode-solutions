# LeetCode Problem: 2379. Minimum Recolors To Get K Consecutive Black Colors
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-colors/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        first_block = blocks[:k]
        min_recolor = 0
        for color in first_block:
            if color == 'W':
                min_recolor += 1

        if min_recolor == 0:
            return min_recolor

        curr_recolor = min_recolor
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                curr_recolor += 1
            
            if blocks[i - k] == 'W':
                curr_recolor -= 1
            
            min_recolor = min(curr_recolor, min_recolor)
        
        return min_recolor

