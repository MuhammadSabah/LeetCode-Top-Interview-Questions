class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicates = {}
        result = 0
        for num in nums:
            if num in duplicates:
                duplicates[num] += 1
            else:
                duplicates[num] = 1

        for key, value in duplicates.items():
            if value == 1:
                result = key

        return result