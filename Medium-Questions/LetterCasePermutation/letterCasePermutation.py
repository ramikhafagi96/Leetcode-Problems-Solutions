# time o(n^2)
# space o(n)
def letterCasePermutation(S: str) -> List[str]:
    if len(S) == 0:
        return []
    queue = deque()
    # set up the queue to have the first char permutation
    if S[0].isalpha():
        queue.append(S[0].lower())
        queue.append(S[0].upper())
    else:
        queue.append(S[0])
    i = 1
    while i < len(S):
        levelSize = len(queue)
        for _ in range(levelSize):
            currPermutation = queue.popleft()
            if S[i].isalpha():
                queue.append(currPermutation + S[i].lower())
                queue.append(currPermutation + S[i].upper())
            else:
                queue.append(currPermutation + S[i])
        i += 1
    return queue
