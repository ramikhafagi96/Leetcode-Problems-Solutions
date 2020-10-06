# time: o(n)
# space: o(n)

def containsDuplicate(self, nums: List[int]) -> bool:
    characterFrequency = {}
    for num in nums:
        if num not in characterFrequency:
            characterFrequency[num] = 1
        else:
            return True
    return False