class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def search(self,d):
        ptr = self.root
        while ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0


    