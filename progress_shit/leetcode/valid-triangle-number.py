class Solution:
    def triangleNumber(self, nums):
        res, n = 0, len(nums)

        nums.sort()
        
        for i in range(2,n):
            left, right = 0, i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    res+=right-left
                    right-=1
                else:
                    left+=1
        return res

# [2,3,4,4]
            
        