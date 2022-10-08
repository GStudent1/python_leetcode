# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) :
        list=[]
        for item in root:
            print(item)

if __name__ == '__main__':
    root = [1,null,2,3]
    sol=Solution()
    sol.inorderTraversal(root)
