class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        prefix=0
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            count+=dic[prefix-goal]
            dic[prefix]+=1
            
        return count

    [0,1,1,2,2,3]