# LeetCode Problem: 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))

            if sorted_str not in groups:
                groups[sorted_str] = []

            groups[sorted_str].append(string)

        return list(groups.values())