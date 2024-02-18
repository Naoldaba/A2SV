class Solution:
    def isValid(self, s: str) -> bool:
        check=[]
        dic={'(':')','{':'}', '[':']'}
        for i in range(len(s)):
            if s[i] in dic.keys():
                check.append(s[i])
            else:
                if not check:
                    return False
                match=check.pop()
                if dic[match]!=s[i]:
                    return False
        return True if len(check)==0 else False
            
        