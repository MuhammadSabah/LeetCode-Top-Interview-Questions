class Solution:
    def climbStairs(self, n: int) -> int:
        last, second_to_last = 1, 1

        for i in range(n - 1):
            temp = last
            last = last + second_to_last
            second_to_last = temp

        return last
