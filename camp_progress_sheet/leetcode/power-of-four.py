class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        x=1
        while x<n:
            x*=4
            if x==n:
                return True
        return False
        