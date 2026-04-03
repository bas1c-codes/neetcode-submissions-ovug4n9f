class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        top = -1

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i not in pairs:   # opening bracket
                l.append(i)
                top += 1
            else:  # closing bracket
                if top == -1 or l[top] != pairs[i]:
                    return False
                l.pop()
                top -= 1

        return l == []