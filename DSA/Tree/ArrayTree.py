class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def array_to_tree(arr,i ,n):
    if i>=n:
        return None
    
    node = Node(arr[i])
    node.left = array_to_tree(arr,2*i+1,n)
    node.right = array_to_tree(arr,2*i+2,n)
    return node


def display_tree(root,level = 0 , prefix = 'Root: '):
    if root is not None:
        print(' '*(level*4)+prefix+str(root.key))
        if root.left or root.right:
            display_tree(root.left , level+1,"L---")
            display_tree(root.right , level + 1 , "R---")


arr = [1,2,3,4,5,6,7]
n = len(arr)

root = array_to_tree(arr,0,n)
print("Node at index 2: ",root.right.key)
print("left child of node at index 2: ",root.left.left.key)

print("\Binary Tree: ")
display_tree(root)