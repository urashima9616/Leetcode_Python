def comparebst(root1, root2):
    stack1 = []
    node1 = root1
    node2 = root2
    while 1:
        while len(stack1) > 0 or node1:
            if node:
                stack.append(node1)
                node1 = node1.left
            else:
                node1 = stack1.pop()
                val1 = node1.val
                node1 = node1.right
                break
        while len(stack2) > 0 or node2:
            if node2:
                stack.append(node2)
                node2 = node2.left
            else:
                node2 = stack2.pop()
                val2 = node2.val
                node2 = node2.right
                break
        if val1 != val2:
            return False
        if len(stack1) == 0 and node1 is None:
            if len(stack2) > 0:
                return False
        if len(stack2) == 0 and node2 is None:
            if len(stack1) > 0:
                return False
        if len(stack1) == len(stack2) == 0 and not node1 and not node2:
            return True
    
