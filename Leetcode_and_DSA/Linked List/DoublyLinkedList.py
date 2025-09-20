class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value) -> bool:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp

    def prepend(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev

        return temp


if __name__ == "__main__":

    my_linked_list = DoublyLinkedList(4)
    my_linked_list.append(2)

    my_linked_list.print_list()

    print(my_linked_list.pop())
    print(my_linked_list.pop())
    print(my_linked_list.pop())

    my_linked_list.prepend(1)
    my_linked_list.print_list()

    my_linked_list.pop_first()
    print(my_linked_list.print_list())

    print(my_linked_list.get(0))
