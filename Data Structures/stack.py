class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        newNode = Node(data)
        if(self.top == None):
            self.top = newNode
            return self
        newNode.next = self.top
        self.top = newNode
        return self
    def display(self):
        current = self.top
        while(current != None):
            print(current.data)
            current = current.next

    def pop(self):
        if(self.top == None) :
            return False

        unwanted = self.top
        # print(unwanted.data)
        self.top = unwanted.next
        unwanted.next = None
        return unwanted.data





undoStack = Stack()
redoStack = Stack()

str = 'amal prasad'

for i in str:
    undoStack.push(i)

# undoStack.display()
redoStack.push(undoStack.pop())
redoStack.push(undoStack.pop())
redoStack.display()
print('____________')
undoStack.push(redoStack.pop())
undoStack.display()
