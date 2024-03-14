# Example usage
from BST import BST

bst = BST()
bst.insert(100)
bst.insert(50)
bst.insert(300)
bst.insert(25)
bst.insert(80)
bst.insert(200)
bst.insert(350)
bst.insert(13)
bst.insert(30)
bst.insert(60)
bst.insert(90)
bst.insert(150)
bst.insert(270)
bst.insert(310)
bst.insert(400)

bst.print_tree()

# Searching for a value
node = bst.search(200)

if node is not None:
    print("Found:", node.val)
    if node.left:
        print("Left:", node.left.val)
    if node.right:
        print("Right:", node.right.val)
else:
    print("Not found")


bst.delete(270)

bst.print_tree()
# Inorder traversal
bst.inorder()