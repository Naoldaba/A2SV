class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=Counter(s)
        count=0
        Set=set()
        res=[]

        for c in s:
            count+=1
            if c not in Set:
                Set.add(c)
            
            dic[c]-=1

            if dic[c]==0:
                Set.remove(c)

            if not Set:
                res.append(count)
                count=0
        return res