
#tree traversal in binary tree
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

def print_preorder(root):
     if root:

       print(root.key),
       print_preorder(root.left)
       print_preorder(root.right)


    #inorder traversal
def print_inorder(root):
    if root:
       print_inorder(root.left)
       print(root.key),
       print_inorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.key),

#main programe

root=node(5)
root.left=node(1)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(6)
print("preoder  :")
print_preorder(root)
print("inorder  :")
print_inorder(root)
print("postorder :")
print_postorder(root)


