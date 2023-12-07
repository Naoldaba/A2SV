class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict={}
        for i in range(len(nums)):
            num_dict[nums[i]]=1
        for i in range(len(nums)+1):
            if i not in num_dict:
                return i
        