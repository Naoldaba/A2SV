class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for _ in range(n)] for _ in range(n)] 
        # print(board)
        cols=[False]*n
        diags=[False]*(2*n-1)
        anti_diags=[False]*(2*n-1)
        
        ans=[]
        def backtrack(row):
            if row==n:
                ans.append([''.join(row) for row in board])
                return 
            for i in range(n):
                if not cols[i] and not diags[row+i] and not anti_diags[row-i]:
                    board[row][i]="Q"
                    cols[i], diags[row+i], anti_diags[row-i]=True, True, True

                    backtrack(row+1)

                    board[row][i]='.'
                    cols[i], diags[row+i], anti_diags[row-i]= False, False, False

        backtrack(0)
        return ans

        