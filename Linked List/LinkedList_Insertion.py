class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)    # New Block
        new_node.next = self.head     # Next points to null
        self.head = new_node          # Head points from null to data

    def insertat(self, prev_node, new_value):
        """ First we check whether list is empty
        If it is, then we ask user to use Push method."""
        if prev_node is None:
            print("Previous node is empty, use push()")

        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_value

    def printlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(3)
    llist.push(4)
    llist.push(5)
    llist.append(10)
    llist.printlist()
    print()

    new_value = 4
    prev_node = llist.head
    while prev_node and prev_node.data != new_value:
        prev_node = prev_node.next

    if prev_node is None:
        print(f"Node with value {new_value} not found")
    else:
        llist.insertat(prev_node, 11)
        llist.printlist()