class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        fib1=0
        fib2=1
        ans=1
        for i in range(2, n+1):
            ans=fib1+fib2
            fib1=fib2
            fib2=ans
        return ans
