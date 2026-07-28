class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26 #char freq of s1
        s2_counts = [0] * 26 #char freq of s2
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            # add freq of that char to the constant array
            #do the same for the s2 counts for it's chars up to len
            #ord(s[i]) - ord('a') this is the ascii rep of the char
            #add 1 to asgi rep of char in array rep 
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True
        else:
            for i in range(len(s1), len(s2)):
                left_prev_char = ord(s2[i-len(s1)])- ord('a')
                right_new_char = ord(s2[i]) - ord('a')
                s2_counts[left_prev_char] -= 1
                s2_counts[right_new_char] += 1
                if s1_counts == s2_counts:
                    return True
            return False




        