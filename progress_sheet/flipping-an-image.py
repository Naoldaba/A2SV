class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_list=[]
        for i in range(len(image)):
            temp=image[i]
            temp.reverse()
            print(temp)
            for j in range(len(temp)):
                if temp[j]==0:
                    temp[j]=1
                else: 
                    temp[j]=0
            new_list.append(temp)
        return new_list

        