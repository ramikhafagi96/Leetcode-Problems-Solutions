# time o(n)
# space o(n)


from collections import deque
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    tree1 = buildTree(p)
    tree2 = buildTree(q)
    return tree1 == tree2

def buildTree(root: TreeNode) -> List[any]:
    queue = deque()
    queue.append(root)
    tree = [root.val]
    while queue:
        levelSize = len(queue)
        
        for _ in range(levelSize):
            currNode = queue.popleft()
            
            if currNode.left:
                queue.append(currNode.left)
                tree.append(currNode.left.val)
            else:
                tree.append("null")
            
            if currNode.right:
                queue.append(currNode.right)
                tree.append(currNode.right.val)
            else:
                tree.append("null")
            
    return tree
