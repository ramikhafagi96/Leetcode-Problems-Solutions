# Method 1: using dictionary
# time o(n)
# space o(1)

def singleNumber(self, nums: List[int]) -> int:
    charFrequency = {}
    for num in nums:
        if num not in charFrequency:
            charFrequency[num] = 0
        charFrequency[num] += 1
    for key, value in charFrequency.items():
        if value == 1:
            return key


# Method 2: using bit-manipulation
# time o(n)
# space o(1)

def singleNumber(self, nums: List[int]) -> int:
    singleNumber = 0
    for num in nums:
        singleNumber ^= num
    return singleNumber
