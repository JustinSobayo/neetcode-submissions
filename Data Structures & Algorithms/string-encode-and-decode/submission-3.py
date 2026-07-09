class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += (str(len(word)) + '/' + word)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i <len(s):
            j = i
            while s[j] != '/':
                j+=1
            word_len = int(s[i:j])
            decoded.append(s[j + 1 : j + word_len + 1])
            i = j + word_len + 1
        return decoded





