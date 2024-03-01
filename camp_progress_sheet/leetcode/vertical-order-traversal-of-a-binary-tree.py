# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        dic=defaultdict(list)
        queue=deque([(root, 0, 0)])
        Min_val=inf
        Max_val=-inf
        ans=[]

        while queue:
            n=len(queue)

            node=queue.popleft()
            dic[node[2]].append([node[0].val, node[1]])
            Max_val=max(Max_val, node[2])
            Min_val=min(Min_val, node[2])

            
            if node[0].left:
                queue.append((node[0].left, node[1]+1, node[2]-1))
            if node[0].right:
                queue.append((node[0].right, node[1]+1, node[2]+1))
        for i in range(Min_val, Max_val+1):
            dic[i].sort(key= lambda x: (x[1], x[0]))
            ans.append([val for val, x in dic[i]])

        return ans
        