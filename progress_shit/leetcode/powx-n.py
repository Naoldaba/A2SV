class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n>=0:
            def Power(x, n):
                if n==0:
                    return 1
                ans=Power(x, n//2)
                ans*=ans
                print(ans)
                if n%2:
                    ans*=x

                return ans
                
            return Power(x,n)

        else:
            def Power(x, n):
                if n==0:
                    return 1
                ans=Power(x, n//2)
                ans*=ans
                print(ans)
                if n%2:
                    ans*=x

                return ans
                
            return Power(1/x,abs(n))

 
       
        