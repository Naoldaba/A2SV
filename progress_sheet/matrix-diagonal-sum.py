class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][i]
        for j in range(len(mat)):
            ans+=mat[j][len(mat)-j-1]
        return ans-mat[len(mat)//2][len(mat)//2] if len(mat)%2!=0 else ans
            
        