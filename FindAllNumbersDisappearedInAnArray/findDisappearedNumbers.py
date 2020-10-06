# Method 1: using sets
# time o(n)
# space o(n)

def findDisappearedNumbers(nums):
    IncompleteRangeSet = set(nums)
    completeRangeSet = set()
    for i in range(len(nums)):
        completeRangeSet.add(i+1)
    diff = completeRangeSet - IncompleteRangeSet
    return diff

# Method 2: in-place using range property
# time o(n)
# space o(1)


def findDisappearedNumbers(nums):
    disappearedNumbers = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1
    print(disappearedNumbers)
    for i, num in enumerate(nums):
        if num > 0:
            disappearedNumbers.append(i+1)
    return disappearedNumbers
