class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        Open, Close=0,0
        for i in range(len(s)):
            if s[i]=="(":
                Open+=1
            elif s[i]==")":
                if Open==0:
                    Close+=1
                else:
                    Open-=1
        return Open+Close