class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):

        new_node = Node(data)
        node = self.head

        # Get to the last node
        previous = None
        while node is not None:
            node = node.next
            if node is None:
                previous.next = new_node

            previous = node

    def print_list(self):
        node = self.head

        while node:
            print(f"{node.data} ->", end=" ")
            node = node.next
        print("None")


ll = LinkedList()

first_node = Node("A")
second_node = Node("B")
third_node = Node("C")

first_node.next = second_node
second_node.next = third_node

ll.head = first_node

ll.print_list()

ll.add("D")
ll.add("E")

ll.print_list()
