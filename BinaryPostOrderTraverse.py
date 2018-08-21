def treePostOrder(root):
    if not root:
        return
    stack = []
    node = root
    while len(stack) > 0 or node:
        if node:
            stack.append(node)
            node = node.right
        else:
            node = stack.pop()
            #visit node
            node = node.left
    