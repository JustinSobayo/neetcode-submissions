class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '/' + word
        return encoded
    #4/WORD10/Solutionno
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j] != '/':
                j+=1
            length = int(s[i:j])
            decoded.append(s[j + 1 : j + length + 1])
            i = j + 1 + length
        return decoded


             

