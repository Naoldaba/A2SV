class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix=[0]
        penality_arr=[]
        for i in range(len(customers)):
            if customers[i]=="Y":
                prefix.append(1)
            else:
                prefix.append(0)
        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]
        Min=float('inf')
        for i in range(len(prefix)):
            Num_Y=prefix[-1]-prefix[i]
            Num_N=i-prefix[i]
            penality = Num_Y+Num_N
            Min=min(Min, penality)
            penality_arr.append(Min)
        ind=penality_arr.index(Min)
        return ind


# [0,1,2,2,3]

        