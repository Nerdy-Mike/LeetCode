# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# For example: 
#   aba is True
#   abc is False

# When you realise you can't even solve easy problem LOL. 
# Time complexity of O(N)
# Space complexity O(1)

class Solution:
    def validPaindrome(self, s: str) -> bool:
        #define helper function
        def check(str,i,j):
            while i<j:
                if str[i] != str[j]:
                    return False
                i +=1
                j -=1

        i = 0
        j = len(s) - 1
        while i<j:
            if s[i] != s[j]:
                return check(s,i,j-1) or check(s,i+1,j)
            i+=1
            j-=1
        return True


