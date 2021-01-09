# Implementation: Stacks and Queues.
## Challenge:

Create a class Stack which has a top property and creates empty class when initiated. THis class should have classic Stack methods like pop, push, peek and the method isEmpty that return True if Stack object is empty Create a class Queue whic has a top property and creates empty class when initiated. This class should have classic Stack methods like pop, push, peek and the method isEmpty that return True if Stack object is empty that has classic methods enqueue, dequeue, peek, isEmpty

## Approach & Efficiency
### Stack:

 * .pop(value) - space and time O(1)
 * .push() - space and time O(1)
 * .peek() - space and time O(1)
 * .is_empty() space and time O(1)
### Queue:

 * .enqueue(value) - space and time O(1)
 * .dequeue() - space and time O(1)
 * .peek - space and time O(1)
 * .is_empty() - space and time O(1)
### API
class Node - Class for the Node instances

Class Stack - which implements Stack data structure with its common methods

 * .is_empty() - Method to check if Stack is empty
 * .push(value) - Method takes any value as an argument and adds a new node with that value to the top of the stack
 * .pop() - Method that removes the node from the top of the stack, and returns the node’s value.
 * .peek() - Method that returns the value of the node located on top of the stack, without removing it from the stack.
class Queue - which implements Queue data structure with its common methods

 * .is_empty() - method to check if Queue is empty
 * .enqueue(value) - method that takes any value as an argument and adds a new node with that value to the back of the queue
 * .dequeue() - Method that removes the node from the front of the queue, and returns the node’s value.
* .peek() - Method that returns the value of the node located in the front of the queue, without removing it from the queue.