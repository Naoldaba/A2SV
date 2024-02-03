class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[nums[0]]
        for num in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[num])
        return prefix_sum