from node import *

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)

        if (self.tail == None):
           self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        if (self.head == None):
            self.head = newNode
            return

    def remove(self, value):
        if (self.head == None):
            return

        if (self.head.value == value):
            self.head = self.head.next # move head
            return

        currentNode = self.head
        while currentNode.next != None:
            if (currentNode.next.value == value):
                currentNode.next = currentNode.next.next # unlink the next node by skipping it
                return
            currentNode = currentNode.next

    def find(self, value):
        if (self.head == None):
            return None

        if (self.head.value == value):
            return self.head

        currentNode = self.head
        while (currentNode.next != None):
            if (currentNode.next.value == value):
                return currentNode.next

            currentNode = currentNode.next

    def print(self):
        if (self.head == None):
            print("List is empty!")
            return

        currentNode = self.head
        while (currentNode != None):
            print(currentNode)
            currentNode = currentNode.next