class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_box(board, x, y):
            d = {}
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in d:
                        return 
                    d[board[i][j]] = 1
            return 1

        def valid_row(board, x):
            d = {}
            for j in range(9):
                if board[x][j] == '.':
                    continue
                if board[x][j] in d:
                    return
                d[board[x][j]] = 1
            return 1
        
        def valid_column(board, y):
            d = {}
            for i in range(9):
                if board[i][y] == '.':
                    continue
                if board[i][y] in d:
                    return 
                d[board[i][y]] = 1
            return 1
        
        # checking if each box is valid
        for i in range(3):
            for j in range(3):
                if not valid_box(board, 3*i, 3*j):
                    return
        
        # checking if each row and column is valid
        for i in range(9):
            if not valid_column(board, i):
                return
            if not valid_row(board, i):
                return
        
        return 1