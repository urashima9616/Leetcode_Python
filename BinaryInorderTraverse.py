#Non-recursive way
def treeinorder(root):
    stack = []
    node = root
    while len(stack) > 0 or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            #visit node
            node = node.right

