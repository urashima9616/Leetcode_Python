#Non-recursive way
def treePreorder(root):
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            res.append(node.right)
        if node.left:
            res.append(node.left)
        
