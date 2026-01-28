class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length=len(s)-1
        start=0


        while(start<length):
            while not s[start].isalnum() and start<length:
                start+=1

            while not s[length].isalnum() and start <length:
                length-=1
            
            if s[start].lower()!=s[length].lower() :
                return False

            
            length=length-1
            start+=1
        return True
        