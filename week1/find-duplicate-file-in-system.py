class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        Map=defaultdict(list)
        ans=[]
        for path in paths:
            spl_list= path.split(" ")
            for i in range(1, len(spl_list)):
                file_name, content= spl_list[i].split("(")
                route=spl_list[0]+"/"+file_name
                Map[content[:-1]].append(route)
        for content, route in Map.items():
            if len(Map[content])>1:
                ans.append(route)
        return ans


            




        