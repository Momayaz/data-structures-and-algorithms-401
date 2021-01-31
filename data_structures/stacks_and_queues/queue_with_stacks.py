class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

############################################

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            raise AttributeError("Queue is empty")
        dequeued = self.front.value
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return(dequeued)

    def peek(self):
        if self.front == None:
            raise AttributeError("Queue is empty")
        return self.front.value

    def isEmpty(self):
        if self.rear:
            return False
        return True

    def __str__(self):
        queue_str = ""
        if self.front:
            current = self.front
            while(current):
                queue_str += f"{ current.value } <- "
                current = current.next
        queue_str += "NULL"
        return (queue_str)
                
###############################################
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise AttributeError("Stack is empty")
        popped = self.top.value
        self.top = self.top.next
        return(popped)

    def peek(self):
        if self.top == None:
            raise AttributeError("Stack is empty.")
        return self.top.value
   

    def isEmpty(self):
        if self.top:
            return False
        return True

    def __str__(self):
        stack_str = ""
        if self.top:
            current = self.top
            while(current):
                stack_str += f"{ current.value } | "
                current = current.next
        stack_str += "NULL"
        return (stack_str)

class PseudoQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, value):
        self.inStack.push(value)

    def dequeue(self):
        if (self.inStack.top == None and self.outStack.top == None):
            raise AttributeError("Queue is empty.")
        if (self.outStack.top == None):
            while(self.inStack.top):
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()



if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(0)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

