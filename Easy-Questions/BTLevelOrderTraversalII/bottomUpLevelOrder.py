# Method 1: BFS
# time o(n)
# space o(n)

from collections import deque


def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []
    result = deque()
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)
    return result

# Method 2: DFS
# time o(n)
# space o(height)


def levelOrderBottom2(root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        dfs(root, 0, result)
        result.reverse()
        return result

def dfs(root: TreeNode,level: int, res: List[List[int]]) -> None:
    if root is None:
        return
    if level >= len(res):
        res.append([])
    res[level].append(root.val)
    dfs(root.left, level+1, res)
    dfs(root.right, level+1, res)
