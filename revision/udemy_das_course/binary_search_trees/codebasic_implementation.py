class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if self.data == data:
            return # node already exist
        
        if data < self.data:
            #insert into left subtree
            if self.left:
                self.left.add_child(data)
            else: 
                self.left = BinarySearchTreeNode(data)    
            
        else: 
            if self.right:
                self.right.add_child(data)
            else: 
                self.right = BinarySearchTreeNode(data)
                
        
if __name__ == '__main__':
    root = BinarySearchTreeNode(5)
    root.add_child(2)
    root.add_child(9)
    root.add_child(5)