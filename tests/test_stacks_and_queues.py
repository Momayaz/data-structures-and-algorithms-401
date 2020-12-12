from data_structures_and_algorithms_401.stacks_and_qeueus.stacks_and_queues import Node, Stack, Queue


def create_stack(nodes):
    """helper function to create a stack"""
    test_stack = Stack()
    for el in nodes:
        test_stack.push(el)
    return test_stack


def test_Node_created():
    node_a = Node('a')
    assert 'a' == node_a.value
    assert None == node_a.next

def test_stack_empty():
    test_stack = Stack()
    assert test_stack.top == None

def test_stack_push():

    test_stack = Stack()
    assert test_stack.top == None
    test_stack.push(5)
    assert test_stack.top.value == 5
    test_stack.push('b')
    assert test_stack.top.value == 'b'
    test_stack.push('c')
    assert test_stack.top.value == 'c'

def test_stack_pop():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.pop() == 'd'
    assert test_stack.top.value == 'c'
    assert test_stack.top.next.value == 'b'
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.peek() == None

def test_stack_peek():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.peek() == 'd'
    test_stack.pop()
    assert test_stack.peek() == 'c'
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.peek() == None

def test_stack_is_empty():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.is_empty() == False
    test_stack = Stack()
    assert test_stack.is_empty() == True


def create_queue(nodes):
    """helper function to create a queue"""
    test_queue = Queue()
    for el in nodes:
        test_queue.enqueue(el)
    return test_queue


def test_queue_empty():
    test_queue = Queue()
    assert test_queue.front == None
    assert test_queue.rear == None

def test_queue_enqueu():
    test_queue = Queue()
    assert test_queue.front == None
    test_queue.enqueue(5)
    assert test_queue.front.value == 5
    test_queue.enqueue('b')
    assert test_queue.rear.value == 'b'
    assert test_queue.front.value == 5
    test_queue.enqueue('c')
    assert test_queue.rear.value == 'c'
    assert test_queue.front.value == 5

def test_queue_dequeue():
    test_queue = create_queue(['a', 'b', 'c', 'd'])
    assert test_queue.dequeue() == 'a'
    assert test_queue.front.value == 'b'
    assert test_queue.front.next.value == 'c'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.peek() == None

def test_queue_peek():
    test_queue = create_queue(['a', 'b', 'c', 'd'])
    assert test_queue.peek() == 'a'
    test_queue.dequeue()
    assert test_queue.peek() == 'b'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.peek() == None

def test_queue_is_empty():
    test_queue = create_queue(['a', 'b', 'c', 'd'])
    assert test_queue.is_empty() == False
    test_queue = Stack()
    assert test_queue.is_empty() == True

def test_queue_one_el():

    test_queue = create_queue([1])

    assert test_queue.is_empty() == False
    assert test_queue.rear.value == 1
    assert test_queue.front.value == 1
