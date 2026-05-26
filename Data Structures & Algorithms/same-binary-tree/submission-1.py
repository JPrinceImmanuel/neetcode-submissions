# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        

        # def dfs(p, res):
        #     if not root:
        #         return 
            
        #     left = dfs(root.left, res)
        #     res.append(root.val)
        #     right = dfs(root.left, res)

        # dfs(p, res_p)
        # dfs(q, res_q)

        # return res_p == res_q
            
        