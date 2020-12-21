
"""Node"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""BT"""
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


    def inOrder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)
            return output

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output

    def postOrder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)
            return output

        if self.root:    
            _walk(self.root)
        else:
            raise AttributeError("Tree is empty.")

        return output
## Breadth First Method:

def breadth_first_traversal(root): 
  
    breadth, result = [], []
    
    if root:
        result.append(root)
    while len(result) > 0:
        current = result.pop(0)
        breadth.append(current.value)
        if current.left:
            result.append(current.left)
        if current.right:
            result.append(current.right)
            
    return breadth


## dunder name caller:

if __name__ == "__main__":

    """BT"""
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    print("Pre-Order: ", bt.preOrder())
    print("In-Order: ", bt.inOrder())
    print("Post-Order: ", bt.postOrder())