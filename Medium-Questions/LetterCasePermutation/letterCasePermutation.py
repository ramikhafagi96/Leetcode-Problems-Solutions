# time o(2^n*n)
    # Explanation:
        # In the outer loop we process each character in the input string one time
        # For each iteration the length of the queue grows exponentially wrt. the length of the string
        # if the input has 3 alphabet characters then the output list length is 2^3=8
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
