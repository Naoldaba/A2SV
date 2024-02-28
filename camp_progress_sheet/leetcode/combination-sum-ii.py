class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        unique=set()
        candidates.sort()
        # print(candidates)

        def backtrack(ind, curr):
            if sum(curr)==target:
                if tuple(curr) not in unique:
                    ans.append(curr.copy())
                    unique.add(tuple(curr))
                return 
                
            if ind==len(candidates) or sum(curr)>target:
                return
            
            for i in range(ind, len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])

        return ans
        return []


        