class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

# Changes the object representation. From memory address to something that you define in the return statement
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


class LinkedList:

    """
    Singly linked list
    """

    head = None

    def __init__(self) -> None:
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                # print('Entered this block')
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the nr of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Return the node or `None` if not found
        Takes O(n) time
        """
        current = self.head

        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):

        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point
        takes O(n) time

        Takes overall O(n) - linear time
        """
        current = self.head

        if index == 0:
            self.add(data)

        if index > 0:

            new_node = Node(data)
            i = 0
            while i != index - 1:
                current = current.next_node
                i = i+1

            previous_current = current
            next_node = current.next_node

            previous_current.next_node = new_node
            new_node.next_node = next_node

    def remove(self, index):
        current = self.head

        if index == 0:
            if current is None:
                raise Exception("Cannot execute delete on an empty list")
        
            self.head = current.next_node

        if index > 0:

            i = 0
            while i != index - 1:
                current = current.next_node
                i = i+1

            previous_current = current
            folloup_node = current.next_node

            previous_current.next_node = folloup_node.next_node
