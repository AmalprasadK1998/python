class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
        self.tail = None

    def create_linked_nodes(self,values):

        if self.head == None:
            self.head=Node(values[0])

        temp = self.head
        i=1

        while i < len(values):
            temp.next = Node(values[i])
            temp=temp.next
            i+=1

        temp=self.head
        while temp:
            print(f"{temp.data}-->",end="")
            temp = temp.next
        print()



    def checkL(self):
        print(self.head.next.next.next.next.next.next.next.data)




ll=linked_list()
ll.create_linked_nodes([1,2,4,5,77,89,3,4])
ll.checkL()