class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        l1 = len(haystack)
        l2 = len(needle)

        if l1 < l2: return -1

        for i in range(l1 - l2 + 1):
            print(haystack[i:i + l2])
            if haystack[i:i + l2] == needle:
                return i

        return -1

