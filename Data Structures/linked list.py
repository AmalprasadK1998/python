


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None


class Linked_list:
    def __init__(self):
        self.head = None

    #  insertion_at beginning
    def add_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# code execution starts here!
if __name__ == '__main__':
    ll = Linked_list()
    ll.head = Node(148)
    second = Node(22)
    third = Node(315)
    fourth = Node(4)
    fifth = Node(523)

    ll.head.next = second
    second.prev = ll.head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = fifth
    ll.add_at_beginning(32)

    ll.print_list()