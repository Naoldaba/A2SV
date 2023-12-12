class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i, num in enumerate(nums):
            if num in store:
                return [i, store[num]]
            else:
                store[target-num]=i
        
        
        
