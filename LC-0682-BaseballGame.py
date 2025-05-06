# LeetCode Problem: 682. Baseball Game
# https://leetcode.com/problems/baseball-game/


def calPoints(operations):
        stack = []
        for operation in operations:
            if operation.lstrip('-').isdigit():
                stack.append(int(operation))
            elif operation == '+':
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D':
                stack.append(2 * stack[-1])
            elif operation == 'C':
                stack.pop()
        return sum(stack)