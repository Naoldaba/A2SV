class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        dic=defaultdict(int)
        total=0
        Max=0
        for r in range(len(nums)):
            total+=nums[r]
            dic[nums[r]]+=1
            while dic[nums[r]]>1:
                dic[nums[l]]-=1
                total-=nums[l]
                l+=1
            Max=max(Max, total)
        return Max
            
        




