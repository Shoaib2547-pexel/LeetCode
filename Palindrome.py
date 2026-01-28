class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palin=0
        if(x<0):
            y=-x
        else:
            y=x

        while(y>0):
             
             lst_Digit=y%10
             y=y/10

             palin=(palin*10)+lst_Digit

        if(palin==x and -2**31<=palin<=2**31-1):
            if(x<0):
                return False

            else:
                return True
        else:
            return False
        