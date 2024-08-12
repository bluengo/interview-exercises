#!/usr/bin/env python3

"""Length Encoder"""

class LengthEncoder:
    @staticmethod
    def compress(inpt):
        result = []
        count = 1
        for i in range(1, len(inpt)):
            if inpt[i] == inpt[i-1]:
                count += 1
            else:
                result.append(inpt[i-1] + str(count))
                count = 1
        result.append(inpt[-1] + str(count))     
        return "".join(result)

    @staticmethod
    def decompress(inpt):
        result = []
        i = 0
        while i < len(inpt):
            char = inpt[i]
            i += 1
            count = 0
            while i < len(inpt) and inpt[i].isdigit():
                count = int(inpt[i]) + (count * 10)
                i += 1
            result.append(char * count)
        return "".join(result)


if __name__ == "__main__":
    le = LengthEncoder()
    inputs = [
	"aaabbbbbbcccddddddddddddaaaa",
        "aaabbbbbbccddddabbbbbbcccdddddd",
        "aaaaabbbcccaaaabbccccccccddddddddddddddd",
        "aabbcc"
    ]
    
    for input in inputs:
        compressed = le.compress(input)
        print(compressed)
        decompressed = le.decompress(compressed)
        print(decompressed)
        if decompressed == input:
            print("OK")
        print("")
