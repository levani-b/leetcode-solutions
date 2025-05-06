# LeetCode Problem: 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/

def toLowerCase(self, s: str) -> str:
        res = ''
        for char in s:
            asc = ord(char)
            if asc >= 65 and asc <=90:
                asc += 32
                res += chr(asc)
            else:
                res += char
        return res