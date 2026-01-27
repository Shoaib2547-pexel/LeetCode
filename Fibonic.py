class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Constraint
        if(n>=0 or n<=30):


            if n == 0:
                return 0

            if n == 1:
                return 1

            
           
            second_last = 0
            last_term = 1


            for i in range(2, n + 1):
                curr = last_term + second_last
                second_last = last_term
                last_term = curr

            return last_term

        else:
            print("Vlaue should be less then 30 and greater than 0")
            return 0

        