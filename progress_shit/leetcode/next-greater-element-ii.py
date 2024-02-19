class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        mon_stack = []

        for i in range(2*n):
            while mon_stack and nums[mon_stack[-1]] < nums[i%n]:
                result[mon_stack[-1]] = nums[i%n]
                mon_stack.pop()

            if i < n:
                mon_stack.append(i)
        return result