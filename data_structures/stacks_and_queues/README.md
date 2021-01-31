# Stacks and Queues


### Auth: Momayaz Aldoos.

Ih this project, we created a data structure called **Stack** and **Queue** in Python. We used three classes, _Node_ and _Queue_, and _Stack_.

**Node** included the following:

    1. `value`.
    2. `next`.

**Queue** included the following:

    _Attributes_:
         1. `front`.
         2. `rear`.

    _methods_:
        1. `enqueue`: which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
        2. `dequeue`: that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
        3. `peek`: that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
        4. `isEmpty`: that takes no argument, and returns a boolean indicating whether or not the queue is empty.
        5. `__str__`: which prints the queue in this format ` { 3 } <- { 7 } <- NULL `.

**Stack** included the following:

    _Attributes_:
         1. `top`.

    _methods_:
        1. `push`: which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
        2. `pop`: that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
        3. `peek`: that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
        4. `isEmpty`: that takes no argument, and returns a boolean indicating whether or not the stack is empty.
        5. `__str__`: which prints the stack in this format `  3 | 7 | NULL `.

**PseudoQueue** included the following:

    _Attributes_:
         1. `inStack`.
         2. `outStack`.

    _methods_:
        1. `enqueue(value)`: which inserts value into the PseudoQueue, using a first-in, first-out approach.
        2. `dequeue()`: which extracts a value from the PseudoQueue, using a first-in, first-out approach.




**User acceptance tests** are included with the following test cases:

*Queue* test cases:

    1. Can successfully enqueue into a queue
    2. Can successfully enqueue multiple values into a queue
    3. Can successfully dequeue out of a queue the expected value
    4. Can successfully peek into a queue, seeing the expected value
    5. Can successfully empty a queue after multiple dequeues
    6. Can successfully instantiate an empty queue
    7. Calling dequeue or peek on empty queue raises exception

*Stack* test cases:

    1. Can successfully push onto a stack
    2. Can successfully push multiple values onto a stack
    3. Can successfully pop off the stack
    4. Can successfully empty a stack after multiple pops
    5. Can successfully peek the next item on the stack
    6. Can successfully instantiate an empty stack
    7. Calling pop or peek on empty stack raises exception

*PseudoQueue* test cases:

    1. Enqueue into the queue.
    2. Enqueue multiple values into the queue.
    3. Dequeue from the queue.
    4. Dequeue multiple values from the queue.
    5. Raise an exception when dequeuing from an empty queue.

