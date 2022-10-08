import null


class Node:
    """节点类"""
    def __init__(self, data=None,lchild=None,rchild=None):
        self.data = data
        self.lchild =lchild
        self.rchild=rchild

class Create_Tree:
    def inorder(self,root:Node):
        list_inorder=[]
        self.inorder(root.lchild)
        list_inorder.append(root.data)
        self.inorder(root.rchild)

if __name__ == '__main__':
    tree = Node("1", None, Node("2", "3",None))
    root=[1,null,2,4]
    sol=Create_Tree()
    sol.inorder(tree)
