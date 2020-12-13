#还是不理解


def __init__(self):
    self.res = float("-inf")
def maxPathSum(self, root: TreeNode) -> int:
    def find(root):
        if (root is None):
            return 0
        #以下的left和right都是不包含根节点的
        left = max(find(root.left),0)
        right = max(find(root.right),0)
        self.res = max(self.res,left+right+root.val)
        return root.val + max(left,right)
    find(root)
    return self.res