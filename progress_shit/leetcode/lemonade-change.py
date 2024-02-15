class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store=defaultdict(int)
        flag=True

        for i in range(len(bills)):
            store[bills[i]]+=1
            change=bills[i]-5
            while change>=15 and store[10]>0:
                change-=10
                store[10]-=1
            while change>=5 and store[5]>0:
                change-=5
                store[5]-=1
            if change>0:
                flag=False
            print(change)

        return flag
        