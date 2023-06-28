#!/usr/bin/python3
"""Defines a class Node of a singly-linked list"""

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
        return (self.__data)

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
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list

        Returns:
        Node: The next node in the linked list
        """
        return (self.__next_node)

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
        self.__next_node = value

class SinglyLinkedList:
    """
    A class used to represent a singly linked list

    Attributes:
    head (Node): The first node in the linked list
    """

    def __init__(self):
        """
        Constructs all the necessary attributes 
        for the singly linked list object
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct 
        sorted position in the list (increasing order)

        Parameters:
        value (Node): The data to be stored in the new node
        """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new
    def __str__(self):
        """Print the entire list in stdout."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return ('\n'.join(values))
