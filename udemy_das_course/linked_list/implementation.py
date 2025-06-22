class Node:

    def __init__(self, data):
        self.data = data
        self.nextnode = None

    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        # this is the first node of the linked list 
        #  We can access this node exclusively!!!
        self.head = None
        self.num_of_nodes = 0
    # Inscertion
    # O(1) constant running time
    def insert_start(self,data):
        self.num_of_nodes +=1
        new_node = Node(data)

#   the head is null (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        # so this is when the linked list is not empty
        else:
            # we have to update the refrence
            new_node.nextnode = self.head
            self.head = new_node

    def insert_end (self,data):
        self.num_of_nodes +=1
        new_node = Node(data)

        # check is the linked is empty or not
        if self.head is None:
            self.head = new_node

        else:
            # this is when linkedlist is not empty
            actual_node = self.head
    # this is why it had O(N) linear running time
            while actual_node.nextnode is not None:
                actual_node = actual_node.nextnode

        # actual_node is the liast node : so we insert the new_node
        # right after the actual node

        actual_node.nextnode = new_node


    # O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes
    # O(N) linerar running time
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextnode
    # O(N) linear running time 
    def remove(self,data):
        
        # the list is empty
        if self.head is None:
            return 
        
        actual_node = self.head
        # we have to rrack the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous node
        # (here with linked lists it is impossible)
        previous_node = None

        # search for the item we want to remove(data)

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextnode

        # search miss
        if actual_node is None:
            return 
        
        # update the references (so we hace the data we want to remove)
        if previous_node is None:
            self.head = actual_node.nextnode
        else:
            # remove an internal node by updating the pointer
            #  No need to del the node because the garbage collector will do that
            previous_node.nextnode = actual_node.nextnode


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(18)
    linked_list.insert_start('Adam')
    linked_list.insert_start(10)
    linked_list.insert_end(100)
    linked_list.insert_end('hji')
    linked_list.traverse()
    print('---------------------')
    linked_list.remove(100)
    linked_list.traverse()
