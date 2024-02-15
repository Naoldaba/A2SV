class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ops=0
        num=1
        while target>1:
            if maxDoubles and target%2==0:
                maxDoubles-=1
                target//=2
            elif maxDoubles==0:
                return ops+target-1
            else:
                target-=1
            ops+=1
        return ops
        
        