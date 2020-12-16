def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right
    return res