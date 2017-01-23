class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        a = n // 3
        b = n % 3
        if b == 1:
            a = a - 1
            b = 4
        elif b == 2:
            pass
        else:
            b = 1
        return 3**(a) * b

s = Solution()
for i in range(2,58):
    print(s.integerBreak(i))

