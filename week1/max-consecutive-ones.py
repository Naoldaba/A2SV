class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        result=0
        count=0
        for r in range(len(nums)):
            if nums[r]==1:
                count+=1
            if nums[r]==0:
                count=0
            result=max(result, count)
        return result
            