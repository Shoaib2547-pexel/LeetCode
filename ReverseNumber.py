class Solution:
    def reverse(self, x) -> int:
        rev = 0

        # handle sign
        if x < 0:
            y = -x
        else:
            y = x

        while y > 0:
            last_digit = y % 10
            y = y // 10
            rev = rev * 10 + last_digit

        if x < 0:
            rev = -rev

        return rev


S1 = Solution()
print(S1.reverse(-123))
