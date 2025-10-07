# LeetCode Problem: 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows(board):
            for row in board:
                seen = {}
                for num in row:
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen[num] = 1
            return True
        
        def check_columns(board):
            for col in range(len(board[0])):
                seen = {}
                for row in range(len(board)):
                    num = board[row][col]
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen[num] = 1
            return True
        
        def check_boxes(board):
            for start_row in range(0, 9, 3):
                for start_col in range(0, 9, 3):
                    seen = {}
                    for r in range(start_row, start_row + 3):
                        for c in range(start_col, start_col + 3):
                            num = board[r][c]
                            if num == '.':
                                continue
                            if num in seen:
                                return False
                            seen[num] = 1
            return True


        return check_rows(board) and check_columns(board) and check_boxes(board)
