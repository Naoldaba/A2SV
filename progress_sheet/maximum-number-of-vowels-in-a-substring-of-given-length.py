class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Set={"a","e","i","o","u"}
        count=0
        Max=l=0

        for i in range(k):
            if s[i] in Set:
                count+=1
                Max=max(Max, count)

        for i in range(k,len(s)):
            if s[i] in Set:
                count+=1
            if s[l] in Set:
                count-=1
            Max=max(Max, count)
            l+=1
        return Max

