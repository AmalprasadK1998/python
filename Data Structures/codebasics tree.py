
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,l:list):
        for i in range(len(l)):
            self.children.append(TreeNode(l[i]))
        # child.parent = self

    def traverse(self):
        print(self.data,end=' ')
        for i in self.children:
            print(i.data,end=' ')
        print()



Node_1 = TreeNode(1)
Node_1.add_child([2,3,4])
Node_1.traverse()

Node_2 = TreeNode(2)
Node_2.add_child([3,4])
Node_2.traverse()
