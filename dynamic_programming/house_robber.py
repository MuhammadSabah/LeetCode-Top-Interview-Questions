class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0, nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(dp[i], dp[i - 1] + nums[i]))

        return dp[-1]
