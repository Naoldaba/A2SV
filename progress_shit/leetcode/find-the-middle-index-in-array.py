class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum=0
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])

        right_sum=prefix[-1] - nums[0]
        if right_sum==0:
            return 0
        
        for i in range(1,len(nums)):
            left_sum=prefix[i]
            right_sum-=nums[i]
            if left_sum==right_sum:
                return i
        return -1

#[0,2,5,4,12,16]
            
        
        