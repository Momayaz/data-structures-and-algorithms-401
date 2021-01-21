class Node:
    """ Class for the Node instances"""
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Class Stack wich implements Stack data structure with its common methods"""

    def __init__(self):
        """Initiate class Stack"""

        self.top = None

    def is_empty(self):
        """Method to check if Stack is empty"""
        if self.top == None:
            return True
        return False

    def push(self, value):
        """Method takes any value as an argument and adds a new node with that value to the top of the stack """

        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        """Method that removes the node from the top of the stack, and returns the node’s value."""

        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located on top of the stack, without removing it from the stack."""

        if not self.is_empty():
            return self.top.value
        else:
            return None


class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None
