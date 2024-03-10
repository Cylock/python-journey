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

        return "-> ".join(nodes)

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
        Adds a new Node containing data at the head of the list.
        Adds by prepending.
        Ex: if l = [head:5] -> [tail:4] then l.add(6) = [new_node/head:6] -> [node/old_head:5] -> [tail:4]
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, data):
        """
        Adds a new Node containing data at the tail of the list.
        Adds by appending
        Ex: if l = [head:5] -> [tail:4] then l.add(6) = [head:5] -> [node/old_tail:4] -> [new_node/tail:6]
        """

        new_node = Node(data)

        if self.head is None:
            self.add(data)
        else:
            current = self.head

            # Iterate through the list until it hits the end where
            # current = tail.next_node = None
            # Keeps track of the previous element so that we can change the pointers

            while current is not None:
                previous_current = current
                current = current.next_node

            # Point the old_tail to the new node/new_tail and new_tail to None
            previous_current.next_node = new_node
            new_node.next_node = current

    def searchByKey(self, key):
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

    # Course implementation of searchByIndex

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    def searchByIndex(self, index):
        """
        Search for the first node containing data that matches the index.
        Return the node or `None` if not found.
        Raises exception if index is out of bounds.
        Takes O(n) time
        """

        list_size = self.size()

        if index > list_size - 1:
            raise Exception(
                f"Cannot perform search. Provided index {index} is out of bounds for the list size {list_size}"
            )

        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current
            else:
                i = i + 1
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

        list_size = self.size()

        if index == 0:
            self.add(data)

        if index > 0:

            if index > list_size - 1:
                raise Exception(
                    f"Cannot insert. Provided index {index} is out of bounds for the list size {list_size}"
                )

            new_node = Node(data)
            i = 0
            while i != index - 1:
                current = current.next_node
                i = i + 1

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
                i = i + 1

            previous_current = current
            folloup_node = current.next_node

            previous_current.next_node = folloup_node.next_node
