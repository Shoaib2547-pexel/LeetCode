import math
class Solution:
    def countDigit(self, n):
        count=0
        while(n>0):
            n=n/10
            count+=1
            n=math.floor(n)

        return count


num=4
Count=0
s1=Solution()
Count=s1.countDigit(num)
print(Count)

