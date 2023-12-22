class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        string=[0]*len(flips)
        Max=0
        temp=0
        for i in range(len(flips)):
            temp+=flips[i]
            string[flips[i]-1]=1
            Max=max(Max, flips[i])
            Sum=(Max*(Max+1))//2
            if Sum==temp:
                count+=1
        return count
        