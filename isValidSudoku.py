from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            curColList = [e for e in board[i] if e != "."]
            if len(set(curColList)) != len(curColList):
                return False

            curRowList = [col[i] for col in board if col[i] != "."]
            if len(set(curRowList)) != len(curRowList):
                return False

        for j in range(3):
            for k in range(3):
                curSquareList = [board[h][w] for h in range(3 * j, 3 * j + 3) for w in range(3 * k, 3 * k + 3) if board[h][w] != "."]
                if len(set(curSquareList)) != len(curSquareList):
                    return False

        return True


sol = Solution()
print(sol.isValidSudoku(
   [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] 
))
