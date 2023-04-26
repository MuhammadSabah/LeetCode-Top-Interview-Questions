class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2,7,11,15] , 9
        resultMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in resultMap:
                return [resultMap[diff], i]
            else:
                resultMap[num] = i

