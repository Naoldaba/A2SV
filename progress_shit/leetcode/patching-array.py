class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        run_sum=0
        res=0
        if nums[0]!=1:
            run_sum=1
            res=1
        i=0

        while run_sum < n:
            if i < len(nums) and nums[i] <= run_sum+1:
                run_sum+=nums[i]
                i+=1
            else:
                run_sum+=run_sum+1
                res+=1
        return res

        