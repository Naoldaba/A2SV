class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max=0
        j=0
        dic=defaultdict(int)
        for i in range(len(s)):
            dic[s[i]]+=1
            while dic[s[i]]>1:
                dic[s[j]]-=1
                j+=1
            Max=max(Max, i-j+1)
        return Max


        