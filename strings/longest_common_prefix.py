class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        if len(strs) == 0 or strs is None:
            return lcp

        min_string = min(strs, key=len)

        for i in range(0, len(min_string)):
            currStr = strs[0][i]
            for j in range(0, len(strs)):
                if currStr != strs[j][i]:
                    return lcp

            lcp += currStr
        return lcp