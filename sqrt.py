class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 1
        end = x
        while(1):
            temp = (start+end)//2
            if temp**2 == x:
                return (start+end)//2
            elif temp**2 < x:
                if start == temp: return temp
                start = temp
            else:
                if end == temp: return temp
                end = temp

s = Solution()
for i in range(0,100):
    print(s.mySqrt(i**2))