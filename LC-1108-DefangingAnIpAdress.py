# LeetCode Problem: 1108. Defanging An IP Address
# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address: str) -> str:
        res = ''
        for char in address:
            if char == '.':
                res += '[.]'
            else:
                res += char
        return res