class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                print(s[i], s[j])
                i +=1
                j -=1
            else:
                print(f"these two dont match {s[i]} and {s[j]} so we are going to check if {s[i+1]} and {s[j]} match or {s[i]} and {s[j-1]} match")
                skip_left = s[i+1:j+1]
                skip_right = s[i:j]
                if skip_left == skip_left[::-1]:
                    return True
                elif skip_right == skip_right[::-1]:
                    return True
                else:
                    return False
        return True        