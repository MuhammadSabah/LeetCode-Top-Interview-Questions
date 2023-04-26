class Solution:
    def myAtoi(self, s: str) -> int:

        if s is None or len(s) < 1:
            return 0

        MAX = 2147483647
        MIN = -2147483648

        s = s.strip()

        is_negative = len(s) >= 1 and s[0] == '-'
        is_positive = len(s) >= 1 and s[0] == '+'

        num = 0
        i = 0

        if is_negative or is_positive:
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if is_negative:
            num = -num

        if num < MIN:
            return MIN

        if num > MAX:
            return MAX

        return num


