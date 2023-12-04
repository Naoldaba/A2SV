class Solution:
    def printVertically(self, s: str) -> List[str]:
        li=s.split(" ")
        Max_string=max(li, key=len)
        ans=[]
        for i in range(len(Max_string)):
            temp=""
            for j in range(len(li)):
                if i<len(li[j]):
                    temp+=li[j][i]
                else:
                    temp+=" "
            temp=temp.rstrip()
            ans.append(temp)
        return ans





        