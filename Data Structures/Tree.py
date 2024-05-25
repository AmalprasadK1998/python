class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


    def add_child(self, child):
        self.children.append(child)

    # recursion!
    def remove_child(self, child):
        self.children.remove(child)

    def traverse(self):
        print(self.data)
        for child in self.children:
            child.traverse()

root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")
root.add_child(child1)
root.add_child(child2)
child2.add_child(child3)

root.traverse()
# Output:
# A
# B
# C
# D
