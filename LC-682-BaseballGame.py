# https://leetcode.com/problems/baseball-game/

def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        sum = 0
        for num in stack:
            sum += num
        return sum