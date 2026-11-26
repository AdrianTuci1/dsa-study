# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode.

class Codec:
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += s.replace(':', '::') + ':;'
        return encoded

    def decode(self, strs):
        decoded = []
        i = 0
        while i < len(s):
            end = s.find(':;', i)
            if end == -1:
                end = len(s)
            decoded.append(s[i:end].replace('::', ':'))
            i = end + 2
        return decoded


codec = Codec()

input1 = ["lint", "code", "love", "you"]
encoded1 = codec.encode(input1)
decoded1 = codec.decode(encoded1)
print(decoded1)

# ['lint', 'code', 'love', 'you']