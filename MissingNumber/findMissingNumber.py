# Method 1: using sets
# time o(n)
# space o(n)

def missingNumber(self, nums: List[int]) -> int:
        numsRangeSet = set()
        for i in range(len(nums)):
            numsRangeSet.add(i+1)
        missingNumber = numsRangeSet.difference(set(nums)).pop()
        return missingNumber

# Method 2: in-place using range summation formula
# time o(n)
# space o(1)

def missingNumber(self, nums: List[int]) -> int:
        trueSum = (len(nums)*(len(nums)+1))/2
        actualSum = sum(nums)
        return int(trueSum - actualSum)
