class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        k=len(p)
        nums_s=Counter(s[:k])
        nums_p=Counter(p)
        anagrams=[]
        if nums_s==nums_p:
            anagrams.append(0)
        for i in range(k, n):
            nums_s[s[i-k]]-=1
            nums_s[s[i]]+=1
            
            if nums_s==nums_p:
                anagrams.append(i-k+1)
        return anagrams


        