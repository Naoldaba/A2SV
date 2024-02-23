class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # reachable_ind=0
        # for i in range(len(nums)-1):
        #     if nums[i]+i >= len(nums-1):
        #         reachable_ind=max(reachable_ind, i+nums[i])

        goal=len(nums)-1
        for i in range(len(nums)-2, -1,-1):
            if nums[i]+i>=goal:
                goal=i
        if goal==0:
            return True
        return False


        