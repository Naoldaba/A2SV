class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i], temp+nums[i])
            if temp>ans:
                ans=temp
        return ans