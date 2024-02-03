class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ''
        t_map=Counter(t)
        s_map=defaultdict(int)
        l=count=0
        ans=float('inf')
        res=""
        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]]+=1
                if s_map[s[r]] == t_map[s[r]]:
                    count+=1
                    while count==len(t_map):
                        if r-l+1 < ans:
                            ans=r-l+1
                            res=s[l:r+1]

                        if s[l] in s_map:
                            s_map[s[l]]-=1

                            if s_map[s[l]]<t_map[s[l]]:
                                count-=1
                        l+=1
        return res



        