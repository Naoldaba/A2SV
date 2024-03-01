class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[]

        board=[['.' for _ in range(n)] for _ in range(n)]
        cols=[False]*n
        diags=[False]*(2*n-1)
        anti_diags=[False]*(2*n-1)

        def backtrack(row):
            if row==n:
                res.append([''.join(row) for row in board])
                return

            for col in range(n):
                if not cols[col] and not diags[col+row] and not anti_diags[row-col]:
                    board[row][col]="Q"
                    cols[col], diags[row+col], anti_diags[row-col]=True, True, True

                    backtrack(row+1)

                    board[row][col]='.'
                    cols[col], diags[row+col], anti_diags[row-col]=False, False, False

        backtrack(0)
        return len(res)
        