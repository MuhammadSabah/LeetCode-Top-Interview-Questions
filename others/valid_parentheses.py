class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        brackets_map = {
            ")": "(",
            "}": "{",
            "]": '['
        }

        for c in s:
            if c in brackets_map:
                if stack and stack[-1] == brackets_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0