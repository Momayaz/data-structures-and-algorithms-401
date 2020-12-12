class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,value):
        node = Node(value)
        if self.head ==None:
            self.head = node
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next =  node

    def insertBefore(self, value, newValue):
        node = Node(newValue)
        current = self.head
        while current.next:
            if current.next.value == value:
                node.next = current.next
                current = node
                return
            else:
                current = current.next

    def insertAfter(self, value, newValue):
        node = Node(newValue)
        current = self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                node.next = current.next
                return
            else:
                current = current.next


if __name__ == "__main__":

    node1 = Node(5)
    node2 = Node(7)
    node3=Node(3)
    node4=Node(4)
    link = LinkedList()
    link.append(node1)
    link.append(node2)
    link.append(node3)
    link.insertAfter(node3,node4)
    print(link)