class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s)) + '/' + s
        return out

    def decode(self, s: str) -> List[str]:
        #until we reach '/' everything before it is the length of the next word
        #take the length of the next word and create a substring with the length in order to store it in the output array
        output = []
        i = 0
        while i < len(s) - 1:
            word_len = ''
            while s[i] != '/' and i < len(s) - 1:
                word_len += s[i]
                i += 1
            j = i + int(word_len)
            output.append(s[i+1 : j + 1])
            i = j + 1
            #now i is pointing to '/'
            #now i have the length of the word
            #i can send another pointer j from where i is curently to word_len to extract the word

        return output
