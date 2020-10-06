# time o(n)
# space o(height)

from collections import deque

def getAverage(nums):
        return float(sum(nums))/len(nums)
def averageOfLevels(root):
    if root is None:
        return [0]
    result = []
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
        result.append(getAverage(currentLevel))
    return result