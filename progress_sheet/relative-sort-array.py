class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr=[]
        count=Counter(arr1)
        print(count)
        for i in range(len(arr2)):
            new_arr+=[arr2[i]]*count[arr2[i]]
            count.pop(arr2[i])
        temp=[]
        if len(count)>0:
            for i,j in count.items():
                temp+=[i]*j
            new_arr.extend(sorted(temp))
        return new_arr
            

        