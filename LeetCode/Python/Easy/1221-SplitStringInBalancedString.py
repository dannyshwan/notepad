class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = cnt = 0

        for char in s:
            cnt += 1 if char == 'R' else -1

            if cnt == 0:
                total += 1

        return total
