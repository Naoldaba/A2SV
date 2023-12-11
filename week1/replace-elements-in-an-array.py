class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store={num:i for i, num in enumerate(nums)}
        for old, new in operations:
            ind=store[old]
            nums[ind]=new
            store[new]=ind
        return nums
        