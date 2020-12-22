class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        output = []

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output


def fizz_Buzz(value):
    if value % 3 == 0:
        return ("Fizz")
    if value % 5 == 0:
        return ("Buzz")
    if value % 3 == 0 and value % 5 == 0:
        return ("Fizz Buzz")
    else:
        return (str(value))


def fizz_buzz_tree(tree):
     
    newTree = BinaryTree()

    if not tree.root:
        return newTree
    
    def fbtree(current):
        node = Node(fizz_buzz_tree(current.value))
        if current.left:
            node.left = fbtree(current.left)
        if current.right:
           node.right = fbtree(current.right)
        return node

    newTree.root = fbtree(tree.root)
    return newTree

if __name__ == "__main__":
    """BT"""
    node = BinaryTree()
    node.root = Node(6)
    node.root.right = Node(5)
    node.root.left = Node(21)
    node.root.right.left = Node(7)
    node.root.left.left = Node(30)
    node.root.right.right = Node(3)
    print("Pre-Order: ", node.preOrder())
    print(fizz_buzz_tree(node).preOrder())
   

    
    