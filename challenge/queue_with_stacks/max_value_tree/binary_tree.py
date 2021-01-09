class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    

def find_maximum_value(root):
    if root == None:
        return float('-inf')
    
    newRoot = root.value
    right_root = find_maximum_value(root.right)
    left_root = find_maximum_value(root.left)

    if (right_root > newRoot):
        newRoot = right_root
    if (left_root > newRoot):
        newRoot = left_root
    return newRoot




if __name__ == "__main__":

    root = Node(1) 
    root.left = Node(7) 
    root.right = Node(5) 
    root.left.right = Node(6) 
    root.left.right.left = Node(1) 
    root.left.right.right = Node(11) 
    root.right.right = Node(9) 
    root.right.right.left = Node(4) 

    print(find_maximum_value(root))