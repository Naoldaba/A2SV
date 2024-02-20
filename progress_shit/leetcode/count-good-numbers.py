class Solution:
    def countGoodNumbers(self, n: int) -> int:

        Mod=10**9+7
        def power(x,y):
            if y==0:return 1

            ans=power(x, y//2)
            ans*=ans
            ans%=Mod
            if y%2: ans*=x
            ans%=Mod

            return ans
        return (power(5,(n//2)+1 if n%2==1 else (n//2) )*power(4, math.floor(n/2))) % Mod

            
        