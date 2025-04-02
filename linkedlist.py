class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at(self, data, position):
        if position == 0:
            self.insert_first(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                return
            temp = temp.next
        if not temp:
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_first(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at(self, position):
        if position == 0:
            self.delete_first()
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp or not temp.next:
                return
            temp = temp.next
        if not temp.next:
            return
        temp.next = temp.next.next

    def get_first(self):
        if not self.head:
            return None
        return self.head.data

    def get_last(self):
        if not self.head:
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.data

    def get_at(self, position):
        temp = self.head
        for _ in range(position):
            if not temp:
                return None
            temp = temp.next
        if not temp:
            return None
        return temp.data

    def update_first(self, new_data):
        if not self.head:
            return
        self.head.data = new_data

    def update_last(self, new_data):
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.data = new_data

    def update_at(self, position, new_data):
        temp = self.head
        for _ in range(position):
            if not temp:
                return
            temp = temp.next
        if not temp:
            return
        temp.data = new_data

    def is_empty(self):
        return self.head is None

    def total_elements(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        if self.is_empty():
            print("The linked list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


ll = LinkedList()

data_positions = [
    ("A", 0),
    ("B", -1),
    ("C", 2),
    ("D", -1),
    ("E", -1)
]

for data, position in data_positions:
    if position == 0:
        ll.insert_first(data)
    elif position == -1:
        ll.insert_last(data)
    else:
        ll.insert_at(data, position)

print("\nInitial Linked List:")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.update_first("X")
print("\nAfter Updating First Element to 'X':")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.update_last("Z")
print("\nAfter Updating Last Element to 'Z':")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.update_at(1, "Y")
print("\nAfter Updating Element at Position 1 to 'Y':")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.delete_first()
print("\nAfter Deleting First Element:")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.delete_last()
print("\nAfter Deleting Last Element:")
ll.print_list()
print("Total Elements:", ll.total_elements())

ll.delete_at(1)
print("\nAfter Deleting Element at Position 1:")
ll.print_list()
print("Total Elements:", ll.total_elements())

print("\nIs the Linked List empty?", ll.is_empty())

print("\nFirst Element:", ll.get_first())
print("Last Element:", ll.get_last())
print("Element at Position 2:", ll.get_at(2))
print("Total Elements:", ll.total_elements())