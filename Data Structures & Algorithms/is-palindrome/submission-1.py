class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = (len(s) - 1)
#["Was it a car or a cat I saw?"]
        while i < j:
            while i < j and True != s[i].isalnum():
                i += 1
            while j > i and True !=s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i +=1
            j-=1
        return True




