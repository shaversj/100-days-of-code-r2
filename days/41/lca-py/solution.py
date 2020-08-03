class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


n1 = Node(6)
n2 = Node(2)
n3 = Node(8)
n4 = Node(0)
n5 = Node(4)
n6 = Node(7)
n7 = Node(9)
n8 = Node(3)
n9 = Node(5)


root = n1
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n5.left = n8
n5.right = n9
n3.left = n6
n3.right = n7

# https://www.youtube.com/watch?v=kulWKd3BUcI


def lowest_common_ancestor(root: Node, p: Node, q: Node):
    if p.data < root.data and q.data < root.data:
        return lowest_common_ancestor(root.left, p, q)
    elif p.data > root.data and q.data > root.data:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root.data


print(lowest_common_ancestor(root, n6, n7))