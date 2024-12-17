class Node:
    def __init__(self, data : int = 0, left = None, right = None):
        self.left = left
        self.data = data
        self.right = right

def preorder_traversal(root : Node):
    print(root.data,end=", ")
    if root.left:
        preorder_traversal(root.left)
    if root.right:
        preorder_traversal(root.right)
    return 

def postorder_traversal(root : Node):
    if root.left:
        postorder_traversal(root.left)
    if root.right:
        postorder_traversal(root.right)
    print(root.data, end=", ")
    return

def inorder_traversal(root : Node):
    if root.left:
        inorder_traversal(root.left)
    print(root.data, end=", ")
    if root.right:
        inorder_traversal(root.right)
    return 

n1 = Node(1,Node(2,Node(4,Node(5,right=Node(6,Node(7))))),Node(3,right=Node(8,Node(9,right=Node(10)))))
"""
                    1
                   / \
                  2   3
                 /     \
                4       8
               /       /
              5       9
               \       \
                6       10
               /
              7   
"""