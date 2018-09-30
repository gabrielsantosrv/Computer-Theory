from binarytree import *

def balance_coeficient(root):
    if root.left == None and root.right == None:
        coef[root.value] = 0
        return 0

    if root.right == None:
        hLeft = balance_coeficient(root.left)
        coef[root.value] = hLeft+1
        return hLeft+1

    if root.left == None:
        hRight = balance_coeficient(root.right)
        coef[root.value] = -hRight-1
        return hRight+1

    hLeft = balance_coeficient(root.left)
    hRight = balance_coeficient(root.right)

    coef[root.value] = hLeft-hRight
    h = max(hLeft, hRight)+1
    return h


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.right.left = Node(5)
root.right.right = Node(6)
print(root)
coef = [0]*root.size

balance_coeficient(root)
print(coef)
