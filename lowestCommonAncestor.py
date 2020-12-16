 def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    self.ans = root
    self.helper(root,p,q)
    return self.ans
def helper(self,root,p,q):
    if root is None:
        return False
    L = self.helper(root.left,p,q)
    R = self.helper(root.right,p,q)
    if ((L or R) and (root == p or root == q)) or (L and R):
        self.ans = root 
    return L or R or (root==p or root==q)
