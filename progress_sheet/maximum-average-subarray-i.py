class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Sum=sum(nums[:k])
        Max=Sum
        for i in range(k,len(nums)):
            Sum+=nums[i]
            Sum-=nums[i-k]
            Max= max(Sum, Max)
        return Max/k
            
        
        
        