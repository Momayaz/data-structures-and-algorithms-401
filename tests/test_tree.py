from data_structures_and_algorithms_401.tree.tree import Node, BinaryTree, BinarySearchTree
import pytest

"""
*BT* Test Cases:
1. Can successfully instantiate an empty tree.
2. Can successfully instantiate a tree with a single root node.
3. Can successfully add a left child and right child to a single root node.
4. Can successfully return a collection from a preorder traversal.
5. Can successfully return a collection from an inorder traversal.
6. Can successfully return a collection from a postorder traversal.
"""

def test_tree_empty():
    bt = BinaryTree()
    assert bt.root == None

def test_tree_single():
    bt = BinaryTree()
    bt.root = Node(7)
    assert bt.root.value == 7

def test_tree_single_left_right():
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(3)
    bt.root.right = Node(2)
    assert bt.root.value == 7
    assert bt.root.left.value == 3
    assert bt.root.right.value == 2
    assert bt.preOrder() == [7, 3, 2]

def test_tree_preorder():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    assert bt.preOrder() == [6, -1, 10, 5, 7, 3]

def test_tree_inorder():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    assert bt.inOrder() == [10, -1, 6, 7, 5, 3]

def test_tree_postorder():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    assert bt.postOrder() == [10, -1, 7, 3, 5, 6]


"""
*BST* Test Cases:
1. Can successfully instantiate an empty BST.
2. Can successfully instantiate a tree with a single root node.
3. Can successfully add multiple nodes to a BST.
4. Can successfully return True when searching for an existing node in BST.
5. Can successfully return False when searching for a non-existing node in BST.
6. Can successfully raise an exception when searching in an empty BST.
"""

def test_bst_empty():
    bst = BinarySearchTree()
    assert bst.root == None

def test_bst_add_single():
    bst = BinarySearchTree()
    bst.add(4)
    assert bst.root.value == 4

def test_bst_add_multiple():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5) 
    assert bst.root.value == 4
    assert bst.root.left.value == -1
    assert bst.root.right.value == 9
    assert bst.root.left.right.value == 3
    assert bst.root.right.left.left.value == 5

def test_bst_contain():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5) 
    assert bst.contains(-1) == True

def test_bst_not_contain():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5) 
    assert bst.contains(7) == False

def test_bst_contain_empty():
    bst = BinarySearchTree()
    with pytest.raises(Exception):
        assert bst.contains(7)