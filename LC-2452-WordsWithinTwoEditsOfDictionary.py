# LeetCode Problem: 2452. Words Within Two Edits Of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for word in queries:
            if word in dictionary:
                res.append(word)
            else:
                for dict_word in dictionary:
                    diff = 0
                    for i in range(len(word)):
                        if word[i] != dict_word[i]:
                            diff += 1
                    if diff <= 2:
                        res.append(word)
                        break
        return res
                    
