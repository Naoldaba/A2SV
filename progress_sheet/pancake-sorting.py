class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        Max=max(arr)
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            Max=max(arr[:i+1])
            pos=arr.index(Max)
            arr[:pos+1]=reversed(arr[:pos+1])
            arr[:i+1]=reversed(arr[:i+1])
            ans.append(pos+1)
            ans.append(i+1)
        return ans

        