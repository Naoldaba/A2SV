class Solution:
    def sortSentence(self, s: str) -> str:
        global r
        result=""
        li=list(s.split(" "))
        new1=[]
        for j in li:
            new1.append(j[::-1])
        new1.sort()
        new2=[]
        for k in new1:
            new2.append(k[::-1])
        for i in new2:
            for m in i:
                if m.isdigit() is False:
                    result+=m
            if i !=new2[len(new2)-1]:
                result+=" "
        return result