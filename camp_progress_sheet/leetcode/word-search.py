class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row_len=len(board)
        col_len=len(board[0])
        path=set()

        def search(ind, r, c):

            if r<0 or c<0 or r>=row_len or c>=col_len or (r,c) in path or board[r][c]!=word[ind]:
                return False
                
            if ind==len(word)-1:
                return True
            
            path.add((r,c))

            ans = (
                  search(ind+1, r+1, c) or 
                  search(ind+1, r-1, c) or 
                  search(ind+1, r, c+1) or 
                  search(ind+1, r, c-1) 
            )
                
            path.remove((r,c))

            return ans
        
        for i in range(row_len):
            for j in range(col_len):
                if search(0, i, j):
                    return True

        return False


        