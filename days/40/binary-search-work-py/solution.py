class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5



def in_order(root: Node):
    # Inorder (Left, Root, Right) : 4 2 5 1 3

    if root:
        # left
        in_order(root.left)
        # root
        print(root.data, end=" ")
        # right
        in_order(root.right)


def pre_order(root: Node):
    # Preorder (Root, Left, Right) : 1 2 4 5 3
    if root:
        # root
        print(root.data, end=" ")
        # left
        pre_order(root.left)
        # right
        pre_order(root.right)


def post_order(root: Node):
    # Postorder (Left, Right, Root) : 4 5 2 3 1
    if root:
        # left
        post_order(root.left)
        # right
        post_order(root.right)
        # root
        print(root.data, end=" ")




in_order(n1)
print()
pre_order(n1)
print()
post_order(n1)

