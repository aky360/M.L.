
"""Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order"""
def preOrderRecursive(root, result): 
    if(not root):
        return 
    result.append(root.data) 
    preOrderRecursive(root.left, result) 
    preOrderRecursive(root.right, result) 


"""Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order"""
def preOrder_iterative(root, result):
    if(not root):
        return
    stack=[]
    stack.append(root) 
    while(stack); 
        node = stack.pop() 
        result.append(node.data) 
        if(node.right): stack.append(node.right) 
        if(node.left): stack.append(node.left) 
