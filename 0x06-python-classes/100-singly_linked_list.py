#!/usr/bin/python3
"""Define singly-linked list"""


class Node:
    """Represent a node in a singly-linked list"""

    def __init__(self, data, new_node=None):
        """Iniatialize a new Node.

        Args:
            data(int): The data of the new Node.
            new_node (Node): The next node of the new Node.
        """
        self.data = dat
        self.new_node = new_node

    @property
    def data(self):
        """set data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @propert
    def new_node(self):
        """set the new_node of the Node"""
        return (self.__new_node)

    @new_node.setter
    def new_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("new_node must be Node object")
        self.__new_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""


    def __init__(self):
        """Iniatlize a linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert New node to the linked list
        Node inserted correctly
        Args:
            value(Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.New_node = None
            self.__head = new
        elif self.__hea.data > value:
            new.new_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.new_node is not None and
                    tmp.new_node.data < value):
                tmp = tmp.new_node
            new.new_node = tmp.new_node
            tmp.new_node = new
    def __str__head
    values = []
    tmp = self.__head
    while tmp is not None:
        values.append(str(tmp.data))
        tmp = tmp.new_node
    return ('\n'.join(values))
