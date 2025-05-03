# LeetCode Problem: 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
        chars_dict = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in chars_dict:
                if stack and stack[-1] == chars_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False 