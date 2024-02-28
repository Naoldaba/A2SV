class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(ind, perm, Set):
            if len(perm)==len(nums):
                ans.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in Set:
                    perm.append(nums[i])
                    Set.add(nums[i])
                    backtrack(i+1, perm, Set)
                    perm.pop()
                    Set.remove(nums[i])

        backtrack(0, [], set())
        return ans
        