class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList:
    def __init__(self):
        # this is the first node of the linked list
        # we can access this node exclusively
        self.head = None
        self.num_of_nodes = 0
    # O(1) constant running time
    def insert_start(self,data):
        self.num_of_nodes +=1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        # so this is when the linked list is not empty
        else: 
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node
    def insert_end(self, data):
        self.num_of_nodes +=1
        new_node = Node(data)
        
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else: 
            # this is when linked list is not empty
            actual_node = self.head 
            
            # this is why it has O(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            
            # actual_node is the last node: So we insert the new_node
            # right after the actual_node
    
    def size_of_list(self):
        return self.num_of_nodes