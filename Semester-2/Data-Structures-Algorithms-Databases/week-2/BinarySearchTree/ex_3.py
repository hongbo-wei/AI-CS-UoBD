from BST import BST

bst = BST()
nodes = [15, 20, 25, 18, 16, 14, 26, 27, 13, 23]

for node in nodes:
    bst.insert(node)

bst.print_tree()