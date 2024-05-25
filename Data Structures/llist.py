class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
        self.tail = None


    def create_linked_nodes(self,values):
        newNode = Node(values)
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
            return self

        self.tail.next = newNode
        self.tail = newNode
        return self
    def display(self):
        current = self.head
        arr = []
        while(current != None):
            arr.append(current.data)
            current = current.next;
        return arr
        # i=0
        # n=[]
        # x = self.head
        #
        # while i<len(values):
        #     x = Node(values[i])
        #     print(f"{x.data}-->", end='')
        #     n.append(x.data)
        #     i+=1
        #     if i<len(values):
        #         x.next = Node(values[i])
        #         x = x.next
        # print()

        # return n

    """def print_llist(self,values):
        f = self.create_linked_nodes(values)
        i = 0
        while i<len(f):
            print(f"{f[i]}-->",end='')
            i+=1
        print()"""

    def is_palindrome(self,values):
        f = self.create_linked_nodes(values)

        i = 0

        flag = True
        while i < len(f):
            if f[i] == f[-i-1]:
                i += 1
                continue
            else:
                flag = False
                break

        if flag == True:
            print("The given linked list is a palindrome")
        else:
            print("The given linked list is not a palindrome")

    def find_duplicates(self,values):
        f = self.create_linked_nodes(values)
        g  = []
        for i in range(len(f)):
            count = 0
            for j in range(len(f)):
                if f[i]==f[j]:
                    count+=1
            if count > 1 and f[i] not in g:
                g.append(f[i])
                print(f"{f[i]} occurs {count} times")

        if count > 1:
            print("Therefore,The linked list has duplicates.")

    def palindrome(self):
       arr = []
       current = self.head
       while(current != None):
           arr.append(current.data)
           current = current.next

       idx = len(arr)
       current = self.head
       while(current != None):
           idx-=1
           if(current.data != arr[idx]):
               return False
           current = current.next

       return True

    def checkL(self):
        print(self.head.next.next.next.data)


    """def is_palindrome(self):
        temp=self.head
        stack=[]
        h = []

        while temp:
            stack.append(temp.data)
            temp=temp.next

        stack1 = stack.copy()

        while stack:
            h.append(stack.pop())

        print(h,stack1)

        if stack1==h:
            print('The given linked list is palindrome')
        else:
            print('The given linked list is not palindrome')"""
#
#
ll=linked_list()
arr = [1,2,2,1]
for i in arr :
    ll.create_linked_nodes(i)
print(ll.display())
print(ll.palindrome())
ll.checkL()

# ll.is_palindrome([1,2,2,1])
# ll.find_duplicates([1,3,4,5,6,6,6,7,6,7])

class BST_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        # can't have duplicates!
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST_Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST_Node(data)