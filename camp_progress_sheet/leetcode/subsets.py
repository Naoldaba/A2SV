class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append([])
        def backtrack(ind, sub):
            if ind==len(nums):
                return
            for i in range(ind, len(nums)):
                sub.append(nums[i])
                res.append(sub.copy())
                backtrack(i+1, sub)
                sub.pop()
        backtrack(0, [])
        return res
        