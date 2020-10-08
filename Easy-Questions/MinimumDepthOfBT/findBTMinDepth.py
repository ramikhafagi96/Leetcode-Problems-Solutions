# Method 1: BFS
# time o(n)
# space o(n)
from collections import deque

def minDepth(root: TreeNode) -> int:
    if root is None:
         return 0
    queue = deque()
    queue.append(root)
    currLevel = 1
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            currNode = queue.popleft()
            if currNode.left is None and currNode.right is None:
                return currLevel
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        currLevel += 1

# Method 2: DFS
# time o(n)
# space o(n)
def minDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    minimumDepth = dfs(root, 1)
    return minimumDepth
    
def dfs(root: TreeNode, currLevel: int) -> int:
    if root is None:
        return inf
    if root.left is None and root.right is None:
        return currLevel
    else:
        return min(dfs(root.left,currLevel+1),dfs(root.right, currLevel+1))