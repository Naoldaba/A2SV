class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        unique=set()

        def backtrack(ind, curr):

            if len(curr) > k or sum(curr)>n:
                return 
            
            if sum(curr) == n and len(curr) == k:
                if tuple(curr) not in unique:
                    res.append(curr.copy())
                    unique.add(tuple(curr))
                return

            for i in range(ind, 10):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()

        backtrack(1, [])
        return res


        