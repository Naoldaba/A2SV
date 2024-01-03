class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        skill.sort()
        arr=[[skill[0],skill[len(skill)-1]]]
        totalSkill=skill[0]+skill[len(skill)-1]
        i=1
        j=len(skill)-2
        ans=0
        while i<=j:
            if totalSkill!=skill[i]+skill[j]:
                return -1
            arr.append([skill[i],skill[j]])
            i+=1
            j-=1
        print(arr)
        for i,j in arr:
            ans+=(i*j)
        return ans
        
        