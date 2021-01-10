class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    def add(self,data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
    def maxNode(self):
        current = self.head
        maximum = self.head.data
        if(self.head == None):
            print("List is empty")
        else:
            while(True):
                if(maximum < current.data):
                    maximum = current.data
                current= current.next
                if(current == self.head):
                    break
        print("Maximum value"+ str(maximum))
cl = List()
cl.add(500)
cl.add(20)
cl.add(10)
cl.add(100)
cl.maxNode()
