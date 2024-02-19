class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack=[]
        ans=[0]*len(temperatures)

        for i in range(len(temperatures)):
            while monotonic_stack and temperatures[monotonic_stack[-1]]<temperatures[i]:
                poped_ind=monotonic_stack.pop()
                ans[poped_ind]=i-poped_ind
            monotonic_stack.append(i)

        return ans

        