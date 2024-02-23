class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if nums==sorted(nums):
            return 0
        ans=0
        last_elem=nums[len(nums)-1]

        for i in range(len(nums)-2,-1,-1):
            spaces=math.ceil(nums[i]/last_elem)
            ans+=(spaces-1)
            last_elem=math.floor(nums[i]/spaces)
        return ans

