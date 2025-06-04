# LeetCode Problem: 3403. Find The Lexicographically Largest String From The Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res:
                res = temp
        return res
