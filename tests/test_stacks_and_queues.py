from data_structures.stacks_and_queues.stacks_and_queues import Stack, Queue

import pytest

"""
*Queue* test cases:
    1. Can successfully enqueue into a queue
    2. Can successfully enqueue multiple values into a queue
    3. Can successfully dequeue out of a queue the expected value
    4. Can successfully peek into a queue, seeing the expected value
    5. Can successfully empty a queue after multiple dequeues
    6. Can successfully instantiate an empty queue
    7. Calling dequeue or peek on empty queue raises exception
"""

def test_enqueue_one():
    queue = Queue()
    queue.enqueue(7)
    assert queue.rear.value == 7

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    assert queue.rear.value == 3
    assert queue.front.value == 7

def test_dequeue():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.front.value == 3

def test_queue_peek():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    assert queue.peek() == 7

def test_is_empty():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    assert queue.isEmpty() == True

def test_init():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None

def test_queue_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        assert queue.dequeue()
    with pytest.raises(Exception):
        assert queue.peek()

###############################################

"""
*Stack* test cases:
    1. Can successfully push onto a stack
    2. Can successfully push multiple values onto a stack
    3. Can successfully pop off the stack
    4. Can successfully empty a stack after multiple pops
    5. Can successfully peek the next item on the stack
    6. Can successfully instantiate an empty stack
    7. Calling pop or peek on empty stack raises exception
"""

def test_push_one():
    stack = Stack()
    stack.push(7)
    assert stack.top.value == 7


def test_push_multiple():
    stack = Stack()
    stack.push(7)
    stack.push(3)
    assert stack.top.value == 3

def test_pop():
    stack = Stack()
    stack.push(7)
    stack.push(3)
    stack.pop()
    assert stack.top.value == 7

def test_pop_empty():
    stack = Stack()
    stack.push(7)
    stack.push(3)
    stack.pop()
    stack.pop()
    assert stack.isEmpty() == True

def test_stack_peek():
    stack = Stack()
    stack.push(7)
    stack.push(3)
    assert stack.peek() == 3

def test_stack_init():
    stack = Stack()
    assert stack.top == None

def test_stack_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        assert stack.pop()
    with pytest.raises(Exception):
        assert stack.peek()



