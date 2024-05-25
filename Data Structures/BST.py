class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if self.data is None:
            self.data = data
            return

        # ignore duplicates!
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def inorder_traversal(self,l=[]):
        # left,root,right!
        if self.left:
            self.left.inorder_traversal(l)

        print(self.data, end=" ")
        l.append(self.data)

        if self.right:
            self.right.inorder_traversal(l)
        return l

    def preorder_traversal(self):
        # root,left,right!
        print(self.data, end=" ")

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        # left,right,root!
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.data, end=" ")

    def search(self, data):

        if self.data == data:
            print(f"{data} is present in this BST!")

        if data < self.data:

            if self.left:
                # identify calls
                # print("left")
                self.left.search(data)

            else:
                print(f"{data} is not found in this BST!")

        if data > self.data:

            if self.right:
                # identify calls
                # print("right")
                self.right.search(data)

            else:
                print(f"{data} is not found in this BST!")

    def deletion(self, data):

        if self is None:
            print("Tree is empty!")
            return

        # If the data to be deleted is smaller than the root's data, then it lies in left subtree
        if data < self.data:

            if self.left:
                self.left = self.left.deletion(data)

            else:
                print("Not found!")
                return self

        # If the data to be deleted is greater than the root's data, then it lies in right subtree
        elif data > self.data:

            if self.right:
                self.right = self.right.deletion(data)

            else:
                print("Not found!")
                return self

        # If data is same as root's data, then this node is to be deleted
        else:

            # Case 1: Node has no children
            if self.left is None and self.right is None:
                self = None
                return None

            # Case 2: Node has one child
            elif self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Case 3: Node has two children
            else:
                # Find the inorder successor
                current = self.right
                while current.left:
                    current = current.left

                self.data = current.data

                # Delete the inorder successor
                self.right = self.right.deletion(current.data)

        return self


    def closest_value(self, target):
        closest = self.data  # start with the root value as the closest
        current = self
        while current:
            if abs(current.data - target) < abs(closest - target):
                closest = current.data  # update the closest value if a closer one is found
            if target < current.data:
                current = current.left  # search in the left subtree
            else:
                current = current.right  # search in the right subtree
        return closest

    def is_bst(self):
        m = self.inorder_traversal()
        return all(m[i] < m[i + 1] for i in range(len(m) - 1))

    





bst_1 = BST(10)
l1 = [10, 6, 3, 1, 7, 98,96]

for i in l1:
    bst_1.insert(i)

print("preorder:", end=" ")
bst_1.preorder_traversal()
print()

print("postorder:", end=" ")
bst_1.postorder_traversal()
print()

print("Inorder:", end=" ")
bst_1.inorder_traversal()
print()

bst_1.search(3)

bst_1.deletion(3)

bst_1.preorder_traversal()
print()

print(bst_1.closest_value(99))


bst = BST(5)
bst.left = BST(7)
bst.right = BST(2)

print(bst.is_bst())  # Output: False



