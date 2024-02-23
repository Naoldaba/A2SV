class Solution:
    def isSymmetric(self, root):
        def dfs(left_node, right_node): 

            if not left_node or not right_node:
                return left_node == right_node
            
            if left_node.val != right_node.val:
                return False

            return dfs(left_node.left, right_node.right) and dfs(left_node.right, right_node.left)

        return dfs(root.left, root.right)