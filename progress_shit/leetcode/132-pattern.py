class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        Min = float('inf')
        stack = []
        for num in nums:

            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:
                return True

            Min = min(Min, num)
            stack.append([num, Min])

        return False
                
        