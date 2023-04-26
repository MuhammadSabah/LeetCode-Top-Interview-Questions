class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31) - 1
        min_int = pow(-2, 31)

        sign = 1
        reversedInt = 0

        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            remainder = x % 10
            x = x // 10
            reversedInt = reversedInt * 10 + remainder

        if not min_int < reversedInt < max_int:
            return 0

        return reversedInt * sign
