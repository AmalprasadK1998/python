class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data == data:
            return
        if self.data < data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        if self.data > data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def preorder(self):
        print(self.data,end=' ')

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data,end=' ')

        if self.right:
            self.right.inorder()


bst = BST(10)
l=[1,4,6,12,13,17]
for i in l:
    bst.insert(i)
bst.inorder()
print()
bst.preorder()