class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        result = False
        for num in nums:
            if num in duplicates:
                result = True
            else:
                duplicates[num] = 1

        return result
