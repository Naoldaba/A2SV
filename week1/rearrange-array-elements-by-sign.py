class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        result=[]
        for i in range(len(nums)):
            if nums[i]==abs(nums[i]):
                even.append(nums[i])
            else:
                nums[i]!=abs(nums[i])
                odd.append(nums[i])
        while len(even)>0 and len(odd)>0:
            result.append(even.pop(0))
            result.append(odd.pop(0))
        if len(even)>0:
            result.extend(even)
        else:
            result.extend(odd)
        return result

