class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next


    def insert_before(self, x, data):
        new_node = Node(data)
        temp = self.head
        if temp is not None:
            if temp.data == x:
                new_node.next = self.head
                self.head = new_node
                return
        while temp:
            if temp.data == x:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = new_node
        new_node.next = temp

    def insert_after(self, x, data):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.data == x:
                break
            temp = temp.next
        if temp is None:
            return
        new_node.next = temp.next
        temp.next = new_node

    def print_reverse(self):
        current = self.head
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=' --> ')

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next


llist = LinkedList()
llist.add_at_end(1)
llist.add_at_end(333)
llist.add_at_end(333)
llist.add_at_end(2)
llist.add_at_end(3)
llist.add_at_beginning(10)
llist.add_at_beginning(9)
llist.add_at_beginning(8)
llist.print_list()
print()
llist.delete_node(2)
llist.print_list()
print()
llist.insert_before(1,23)
llist.insert_after(3,77)
print("Reversed list:")
llist.print_reverse()
print()
print("Original list:")
llist.print_list()

llist.remove_duplicates()
print()
print("List after removing duplicates:")
llist.print_list()


