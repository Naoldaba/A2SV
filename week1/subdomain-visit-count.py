class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        Map=defaultdict(int)
        for dom in cpdomains:
            new_str="".join(dom)
            split_dom=new_str.split(" ")
            Map[split_dom[1]]+=int(split_dom[0])
            sub_doms=split_dom[1].split(".")
            Map[sub_doms[-1]]+=int(split_dom[0])

            if sub_doms[-2]+"."+sub_doms[-1] != split_dom[1]:
                Map[sub_doms[-2]+"."+sub_doms[-1]]+=int(split_dom[0])
        ans=[]
        for dom, times in Map.items():
            ans.append(f'{times} {dom}')
        return ans



            

        