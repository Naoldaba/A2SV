class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append([])
        nums.sort()
        sub=[]
        def backtrack(ind):
            if ind==len(nums):
                return
            for i in range(ind, len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                res.append(sub.copy())
                backtrack(i+1)
                sub.pop()
        backtrack(0)
        return res

        