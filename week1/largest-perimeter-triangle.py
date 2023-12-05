from itertools import combinations
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # def Triangle_Area(li):
        #     a,b,c=li
        #     s=sum(li)/2
        #     area=float((s*(s-a)*(s-b)*(s-c)))
        #     return True if area>0 else False
        # result=0
        # posible_triangles=list(combinations(nums, 3))
        # for triangle in posible_triangles:
        #     if Triangle_Area(triangle):
        #         result=max(result, sum(triangle))
        # return result

        nums.sort()
        n = len(nums)
        
        i = n-3
        j = n-1

        while(i>=0):
            if(nums[i]+nums[i+1]>nums[j]):
                return nums[i]+nums[i+1]+nums[j]
            i-=1
            j-=1
        return 0
        
        