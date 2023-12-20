class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        visited=[]
        r,c=len(mat), len(mat[0])
        i,j=0,0
        north_east=True
        
        while len(visited)<r*c:
            visited.append(mat[i][j])
            if north_east:
                if j==c-1:
                    i+=1
                    north_east=False
                elif i==0:
                    j+=1
                    north_east=False
                else:
                    i-=1
                    j+=1
            else:
                if i==r-1 :
                    j+=1
                    north_east=True
                elif j==0:
                    i+=1
                    north_east=True
                else:
                    i+=1
                    j-=1
        return visited
        