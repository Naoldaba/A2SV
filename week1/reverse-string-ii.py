class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_str=""
        for i in range(0, len(s), 2*k):
            if len(s[i:])>2*k:
                temp=s[i:i+k]
                new_str+=temp[::-1]+s[i+k:i+(2*k)]

            elif len(s[i:])<k:
                temp=s[i:]
                new_str+=temp[::-1]
            elif len(s[i:])>= k:
                temp=s[i:i+k]
                new_str=new_str+temp[::-1]+s[i+k:]     
        return new_str



        