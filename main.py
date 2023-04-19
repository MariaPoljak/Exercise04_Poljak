# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert_node(self, prev_node_data, new_node_data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = SLLNode(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False

    def clear(self):
        while self.head != None:
            current = self.head
            self.head = self.next
            current = None
        return

    def get_data(self, data, node):
        node = self.head
        while node = data:
            node = node.next
            if node is None:
            return False
        return node

    def delete_node(self, data):
        current = self.head
        if current is not None:
            if current.data = data:
                self.head = current.next
                current = None
            return
        while current is not None:
            if current.data == data:
                break
            current.previous = current
            current = current.next
            if current == None:
                return
            current.previous = current.next


#DoublyLinkedList

class DLLNode:
    def __init__(self, data):
        self.head = None
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        current.previous = self.tail
        if self.tail is None:
            self.head = node
            self.tail = node
            node.next = None
        else:
            self.tail.next = node
            node.next = None
            self.tail = node
        self.size += 1


    def insert_node(self, prev_node_data, new_node_data):
        current = self.head
        while current is not None:
            if current.data == prev_node_data:
                new_node = DLLNode(data)
                new_node.next = current.next
                new_node.previous = current
                if current.next is not None:
                    current = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return
            current = current.next
        self.size += 1
        return False

    def delete_node(self, data):
        current = self.head
        if current is not None:
            if current.data = data:
                self.head = current.next
                current = None
            return
        while current is not None:
            if current.data == data:
                break
            current.previous = current
            current = current.next
            if current == None:
                return
            current.previous = current.next

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.next
            temo = None
        return ()

    def get_data(self, data, node):
        node = self.head
        while node = data:
            node = node.next
            if node is None:
            return False
        return node


#MyStack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        node = Node(element)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        return

    def pop(self):
        if self is None:
            raise Exception("The stack is empty.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return

    def size(self):
        return self.size


#MyQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, element):
        if self.tail = None:
            element = self.tail
        return

    def show_left(self):
        if self.tail != None
        return self.tail as int

    def show_right(self):
        if self.head != None
        return self.head as int

    def size(self):
        return self.size as int