# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def Mode(root, List):
            if root:
                List.append(root.val)
                Mode(root.left, List)
                Mode(root.right, List)
            return List

        ans= Mode(root, [])
        print(ans)
        Count=Counter(ans)
        temp=sorted(Count.items(), key=lambda x: x[1], reverse=True) 

        res=[]
        print(temp)
        Max_rep=temp[0][1]
        for i in range(len(temp)):
            if temp[i][1]==Max_rep:
                res.append(temp[i][0])
            else:
                break
        return res


            
        