class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_s1=Counter(s1)
        sub=s2[:len(s1)]
        dic_sub=Counter(sub)
        l=0
        for i in range(len(s1), len(s2), 1):
            print("hi")
            if dic_sub==dic_s1:
                return True
            if s2[l] in dic_sub:
                dic_sub[s2[l]]-=1
            dic_sub[s2[i]]+=1
            l+=1
        if dic_sub==dic_s1:
                return True
        return False



        