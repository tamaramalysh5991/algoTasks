import math

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __str__(self):
        f"val {self.value} -> {self.next.value if self.next else ''}"

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, ref_node, val):
        if ref_node is None:
            return
        new_node = Node(val)
        new_node.next = ref_node.next
        ref_node.next = new_node

    def length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def get_at_index(self, index):
        curr_node = self.head
        if index > self.length() - 1:
            return -1
        for i in range(index):
            if curr_node:
                curr_node = curr_node.next
        return curr_node


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    # [4, 5, 1, 9]
    llist.push(9)
    llist.push(1)
    llist.push(5)
    llist.push(4)
    # delete 5
    node_5 = llist.get_at_index(1)

    node_5.val = node_5.next.value
    node_5.next = node_5.next.next

    print(node_5)