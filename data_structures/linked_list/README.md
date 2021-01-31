# Linked Lists

Ih this project, we created a data structure called **Singly-Linked-List** in Python. We used two classes, _Node_ and _LinkedList_.

**Node** included the following:

    1. `value`.
    2. `next`.

**LinkedList** included the following:

    _Attributes_:
         1. `head`.

    _methods_:
        1. `insert`: takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
        2. `includes`: takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        3. `__str__`: returns a string representing all the values in the Linked List, formatted as: `"{ a } -> { b } -> { c } -> NULL"`
        3. `append`: dds a new node with the given value to the end of the list.
        4. `insertBefore`: adds a new node with the given newValue immediately before the first value node.
        5. `insertAfter`: adds a new node with the given newValue immediately after the first value node.
        6. `deleteValue`:  delete a node with the given value from the linked list.
        7. `get_kth_value`: takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.
        8. `zipLists`: takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists.
        9. `reverseList`: takes a linked list and returns its reverse.

**User acceptance tests** are included with the following test cases:

    1. Can successfully instantiate an empty linked list.
        * list = LinkedList() -> None
    2. Can properly insert into the linked list.
        * list.insert(3) -> { 3 } -> NULL
    3. The head property will properly point to the first node in the linked list.
        * print (list.head.value) -> 3
    4. Can properly insert multiple nodes into the linked list.
        * list.insert(5)
        * list.insert(7)
        * list.insert(9)
    5. Will return true when finding a value within the linked list that exists.
        * list.includes(5) -> True
    6. Will return false when searching for a value in the linked list that does not exist.
        * list.includes(11) -> False
    7. Can properly return a collection of all the values that exist in the linked list.
        * print(list) -> "{ 9 } -> { 7 } -> { 5 } -> { 3 } -> NULL"
        
    8. Can successfully add a node to the end of the linked list.
    9. Can successfully add multiple nodes to the end of a linked list.
    10. Can successfully insert a node before a node located i the middle of a linked list.
    11. Can successfully insert a node before the first node of a linked list.
    12. Can successfully insert after a node in the middle of the linked list.
    13. Can successfully insert a node after the last node of the linked list.
    14. Can successfully delete a value in the middle of the linked list.
    15. Can successfully delete a the first value of the linked list.
    16. Can successfully delete a the last value of the linked list.
    * test `get_kth_value` when:
    1. Where k is greater than the length of the linked list
    2. Where k and the length of the list are the same
    3. Where k is not a positive integer
    4. Where the linked list is of a size 1
    5. “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    * test `zipLists` when:
    1. Where both lists are empty.
    2. Where 1st list is empty.
    3. Where 2nd list is empty.
    4. Where both lists have the same length.
    5. Where 1st fist is longer than the 2nd list.
    6. Where 2nd list is longer than the 1st list.

