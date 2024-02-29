class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        Hash_map={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        n=len(digits)
        ans=[]

        def backtrack(ind, comb):
            if ind==n:
                ans.append(comb)
                return
                
            for i in Hash_map[digits[ind]]:
                backtrack(ind+1, comb+i)

        backtrack(0, "")
        return ans
            



        