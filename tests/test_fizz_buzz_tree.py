from data_structures_and_algorithms_401.fizz_buzz_tree.fizz_buzz_tree import BinaryTree, Node, fizz_buzz_tree,fizz_Buzz
import pytest

def test_fizzbuzz_not_empty():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.right.left = Node(30)
    bt.root.left.left = Node(45)
    bt.root.right.right = Node(3)
    fbt = fizz_buzz_tree(bt)
    assert fbt.preOrder() == ['Fizz', 'Buzz', '7', 'Fizz Buzz', 'Fizz Buzz', 'Fizz']
    
