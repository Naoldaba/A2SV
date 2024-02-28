class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def backtrack(num, combination):
            if len(combination)==k:
                ans.append(combination.copy())
                return 
            for i in range(num, n+1):
                combination.append(i)
                backtrack(i+1, combination)
                combination.pop()

        backtrack(1, [])
        return ans
            
        