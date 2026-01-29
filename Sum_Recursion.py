class Solution(object):
    def Sum(self,n):
        """
        :type n: int
        :rtype: int

        """
        
        if(n==1):
            return 1
        else:
            return n + self.Sum(n-1)
        

Num=5

S1=Solution()
print(S1.Sum(Num))