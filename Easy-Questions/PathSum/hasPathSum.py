# time o(n)
# space o(n)

def hasPathSum(root, sum):
    return dfs(root, 0, sum)
        
def dfs(root, currSum, targetSum):
    if root is None:
        return False
    currSum += root.val
    if root.left is None and root.right is None:
        return currSum == targetSum
    else:
        return dfs(root.left, currSum, targetSum) or dfs(root.right, currSum, targetSum)