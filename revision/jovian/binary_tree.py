'''
basic method

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

node0.left = node1
node0.right = node2

node1.left = node3

node2.left = node4
node2.right = node5

node4.right = node6

node5.left = node7
node5.right = node8



tree = node0

print(tree.right.left.right.key)

'''


tree_tuple = ((1,3,None), 2, ((None,3,4),5,(6,7,8)))
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        
def parse_tuple(data):
    # print('data', data)
    if data is None:
        node = None
    elif isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)



def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

print(traverse_in_order(tree2))