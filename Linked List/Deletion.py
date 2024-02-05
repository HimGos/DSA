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

    def delete_node(self, key):
        temp = self.head               # Pointing to head first

        # Case 1: Node found at first place
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Case 2: Node in middle
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Case 3: Empty list
        if temp is None:
            return

        prev.next = temp.next          # Prev next to next node
        temp = None                    # Free up memory / delete

    def delete_list(self):
        curr = self.head
        while curr:
            next_val = curr.next
            del curr.data
            curr = next_val

    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(4)
    llist.push(8)
    llist.push(12)
    llist.push(1)
    llist.display()
    print()
    llist.delete_node(8)
    llist.display()
    print()
    llist.delete_list()
