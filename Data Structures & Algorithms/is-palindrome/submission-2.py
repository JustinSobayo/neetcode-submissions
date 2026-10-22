class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        while i <= j:
            #get rid of spaces
            while not s[i].isalnum() and i < j:
                if i > j:
                    return True
                else:
                    i +=1
            while not s[j].isalnum() and i < j:
                if i > j:
                    return True
                else:
                    j -=1
            if s[i].lower() == s[j].lower():
                i +=1
                j -=1
            else:
                return False
        return True