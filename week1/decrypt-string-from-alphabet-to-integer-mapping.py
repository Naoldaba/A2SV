class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_str=""
        i=0
        while i<len(s):
            if (i+2 < len(s) and s[i+2]!="#") or i+2>=len(s) :
                new_str+=chr(96+int(s[i]))
                i+=1
            else:
                new_str+=chr(96+int(s[i:i+2]))
                i+=3
        return new_str

