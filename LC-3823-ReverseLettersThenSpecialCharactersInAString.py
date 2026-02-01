# LeetCode Problem: 3823. Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution:
    def reverseByType(self, s: str) -> str:
        chars = []
        letters = []
        list_s = list(s)
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                chars.append(char)

        letters.reverse()
        chars.reverse()

        c = 0
        l = 0
        for i in range(len(list_s)):
            if list_s[i].isalpha():
                list_s[i] = letters[l]
                l += 1
            else:
                list_s[i] = chars[c]
                c+= 1

        return ''.join(list_s)
            