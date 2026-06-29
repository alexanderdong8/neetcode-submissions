class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for x in strs:
            encoded.append(x)
            encoded.append("#@")
        
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        word = []
        x = 0
        while x < len(s):
            if x+1 < len(s) and s[x:x+2] == "#@":
                decoded.append("".join(word))
                x += 2
                word.clear()

            else:
                word.append(s[x])
                x += 1
            
        return decoded


