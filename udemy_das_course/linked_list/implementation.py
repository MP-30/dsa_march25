class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList:
    def __init__(self):
        # this is the first node of linkedlist
        # We can access this node exclusively!!!
        self.head = None
        self.num_of_nodes = 0
    
    # o(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes +=1
        new_node = Node(data)
        
        # the head is NULL (so the data structure is empty)
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
        
        # we have to check if linked list is empty or not
        if self.head is None:
            self.head = new_node
        else:
            # this is when linked list in not empty
            acutal_node = self.head
            
            # this is why it has 0(n) linear running time
            while acutal_node.next_node is not None:
                acutal_node = acutal_node.next_node
                
            # acutal_node is the last node: so we insert the new_node
            # right after the actual_node
            
            
    
        
    # o(1)
    def size_of_list(self):
        return self.num_of_nodes
    