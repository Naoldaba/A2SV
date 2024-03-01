class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        cur=[]
        
        def backtrack(o_c, c_c):
            if o_c==c_c==n:
                ans.append(''.join(cur))
                return 
            if o_c<n:
                cur.append('(')
                backtrack(o_c+1, c_c)
                cur.pop()
            if c_c<o_c:
                cur.append(')')
                backtrack(o_c, c_c+1)
                cur.pop()
        backtrack(0,0)
        return ans

        