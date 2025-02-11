class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,root):
        print("Enter the data:")
        data = int(input())

        if data == -1:
            return None
        
        print('Enter data for inserting in left of ',data)
        root.left = self.buildTree(root.left)