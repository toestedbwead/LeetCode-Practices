# Running Sum of 1d Array
# Topics: Array, Prefix Sum, Weekly Contest 193
# maintains a cumulative total as i iterate through an array
# each position stores the sum of all elements up to that point

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for num in nums:
            total+=num
            result.append(total)
        return result

