class Solution(object):
    def Sum(self,n):
        """
        :type n: int
        :rtype: int

        """
        # Base Case 
        if(n==1):
            return 1
        else:
        # Recursive Case
            return n + self.Sum(n-1)
        

Num=5

S1=Solution()
print(S1.Sum(Num))