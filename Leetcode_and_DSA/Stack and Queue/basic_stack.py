from __future__ import annotations
from typing import Optional, TypeVar, Generic, Iterator

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value) -> None:
        self.value: T = value
        self.next: Optional[Node] = None


class Stack(Generic[T]):

    def __init__(self, value: T) -> None:
        new_node: Node[T] = Node(value)
        self.top: Optional[Node[T]] = new_node
        self.height: int = 1

    def print_stack(self) -> None:
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def __iter__(self) -> Iterator[T]:
        temp = self.top
        while temp:
            yield temp.value
            temp = temp.next

    def print_stack_with_iter(self) -> None:
        for v in self:
            print(v)

    def push(self, value: T) -> None:
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None

        self.height -= 1
        return temp.value


if __name__ == "__main__":

    my_stack = Stack(4)
    my_stack.push(2)

    my_stack.print_stack()

    # my_stack.print_stack_with_iter()
