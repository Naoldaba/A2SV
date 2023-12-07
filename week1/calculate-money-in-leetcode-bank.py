class Solution:
    def totalMoney(self, n: int) -> int:
        w=n//7
        r=n%7
        total=0
        if n>7:
            week_sum = (w/2)*(56+(w-1)*7)
            total+=week_sum
        if r>0:
            rem_sum=(r/2)*(2*(w+1)+(r-1))
            total+=rem_sum
        return int(total)
            
        
