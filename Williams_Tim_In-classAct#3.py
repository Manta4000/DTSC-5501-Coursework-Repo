"DTSC 5501 - In-Class Activity 3 - Linked Lists - Timothy Williams"

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    class LinkedList:

        def __init__(self):
            self.head = None

        def push(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            raise NotImplementedError

        def append(self, value):
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            raise NotImplementedError

        def __str__(self):
            values = []
            current = self.head
            while current:
                values.append(current.data)
                current = current.next
            return " -> ".join(map(str, values))

        def count(self):
            current = self.head
            count = 0
            while current:
                count += 1
                current = current.next
            return count

        def getAt(self,index):
            current = self.head
            for _ in range(index):
                if not current:
                    raise IndexError("Index out of bounds")
                current = current.next
            if not current:
                raise IndexError("Index out of bounds")
            return current.data

        def insertAt(self, index, data):
            if index < 0 or index > self.count():
                raise IndexError("Index out of bounds")
            if index == 0:
                self.push(data)
                return
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

        def removeAt(self, index):
            if index < 0 or index >= self.count():
                raise IndexError("Index our of bounds")
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                current.next = current.next.next

