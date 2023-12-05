class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_copy=nums.copy()
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                nums[i-1]=nums[i]
                nums_copy[i]=nums_copy[i-1]
                break
        return nums==sorted(nums) or nums_copy==sorted(nums_copy)       

        