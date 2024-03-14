from BST import BST

bst = BST()
nodes = [15, 20, 25, 18, 16]

for node in nodes:
    bst.insert(node)

bst.print_tree()