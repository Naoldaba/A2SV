class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[""]*n for _ in range(m)]
        for i,j in guards:
            grid[i][j]="X"
        for i,j in walls:
            grid[i][j]="X"

        def dfs(r,c):
            count=0

            #right
            j=c+1
            while j<n and grid[r][j]!="X":
                if grid[r][j]=="":
                    grid[r][j]="R"
                    count+=1
                j+=1

            #left
            j=c-1
            while j>=0 and grid[r][j]!="X":
                if grid[r][j]=="":
                    grid[r][j]="R"
                    count+=1
                j-=1

            #up
            i=r-1
            while i>=0 and grid[i][c]!="X":
                if grid[i][c]=="":
                    grid[i][c]="R"
                    count+=1
                i-=1

            #down
            i=r+1
            while i<m and grid[i][c]!="X":
                if grid[i][c]=="":
                    grid[i][c]="R"
                    count+=1
                i+=1
            print(count)
            return count

        Watched=0
        for i,j in guards:
            Watched+=dfs(i,j)
        return (m*n)-len(guards)-len(walls)-Watched

        