class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=list(set(nums))
        nums.sort()
        Max=1
        temp=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:  
                temp+=1
            else:
                temp=1
            Max=max(Max, temp)
        return Max
        