class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:

        if len(suffix) == 0:
            return True

        if (
            row < 0
            or row == self.rows
            or col < 0
            or col == self.cols
            or self.board[row][col] != suffix[0]
        ):
            return False

        self.board[row][col] = "*"

        for rowOffset, colOffset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        self.board[row][col] = suffix[0]

        return False