class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data)
        # if(self.front == None):
        #     self.front = new_node
        #     self.rear = new_node
        #     return self
        # self.rear.next = new_node
        # self.rear = new_node
        # return  self
        #

        if(self.front == None):
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def display(self):
        arr = []
        current = self.front
        while(current != None):
            arr.append(current.data)
            current = current.next

        return arr
    def dequeue(self):
        if(self.front == None):
            return False
        unwanted = self.front
        self.front = unwanted.next
        unwanted.next = None
        return unwanted.data




    def print_Queue(self):
        print(self.bottom.data)


    def deque(self):
        pass

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
print(q1.display())