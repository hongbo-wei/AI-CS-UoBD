from AVLTree import AVLTree

tree = AVLTree()
root = None

for value in [40,69,51,76,12,5,3,83,82,88]:
   print ("Inserting ", value)
   root=tree.insert(root, value)
   tree.print_tree(root)
   print()
