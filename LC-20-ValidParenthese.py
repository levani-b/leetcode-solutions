# https://leetcode.com/problems/valid-parentheses/

def isValid(self, s):
        stack = []
        chars_dict = {')': '(', ']': '[', '}' : '{'}
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