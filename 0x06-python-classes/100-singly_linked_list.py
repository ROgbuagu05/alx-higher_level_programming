#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """
    A class used to represent a node of a singly linked list

    Attributes:
    data (int): The data stored in the node
    next_node (Node): The next node in the linked list
    """
    def __init__(self, data, next_node=None):
        """
        Constructs all the necessary attributes for the node object

        Parameters:
        data (int): The data to be stored in the node
        next_node (Node): The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node

        Returns:
        int: The data stored in the node
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node

        Parameters:
        value (int): The data to be stored in the node

        Raises:
        TypeError: If the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list

        Returns:
        Node: The next node in the linked list
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list

        Parameters:
        value (Node): The next node in the linked list

        Raises:
        TypeError: If the value is not a Node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    A class used to represent a singly linked list

    Attributes:
    head (Node): The first node in the linked list
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the singly linked list object
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order)

        Parameters:
        value (int): The data to be stored in the new node
        """
        new_node = Node(value)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # If the new node is smaller than the head, set it as the new head
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        # Traverse the list to find the correct position for the new node
        current_node = self.head
        while current_node.next_node is not None and current_node.next_node.data < value:
            current_node = current_node.next_node

        # Insert the new node into the list
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list

        Returns:
        str: A string representation of the linked list
        """
        current_node = self.head
        linked_list_str = ""
        while current_node is not None:
            linked_list_str += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return (linked_list_str)
