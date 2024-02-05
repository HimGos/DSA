class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        # Step 1
        prev = None
        curr = self.head
        # next = None

        while curr:
            # Step 2
            next = curr.next
            curr.next = prev

            # Step 3
            prev = curr
            curr = next

        self.head = prev

    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next


if __name__ == "__main__":
    link = LinkedList()
    link.push(1)
    link.push(2)
    link.push(3)
    link.push(4)
    link.push(5)
    link.display()
    print()
    link.reverse()
    link.display()