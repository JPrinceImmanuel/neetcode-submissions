# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not (p and q):
            return None

        lower = min(p.val, q.val)
        greater = max(p.val, q.val)

        if root.val > greater:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < lower:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val <= greater and root.val >= lower:
            return root