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

    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next

    def node_count(self, node):   # Using Recursion
        if not node:
            return 0
        else:
            return 1 + self.node_count(node.next)

    def getcount(self):
        return self.node_count(self.head)

    def iterativecount(self):     # Using Iteration
        count = 0
        tmp = self.head
        while tmp:
            count += 1
            tmp = tmp.next
        return count


if __name__ == "__main__":
    l = LinkedList()
    l.push(1)
    l.push(5)
    l.push(51)
    l.push(545)
    l.push(523)
    print(l.getcount())
    print(l.iterativecount())