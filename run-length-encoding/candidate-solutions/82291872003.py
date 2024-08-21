#!/usr/bin/env python3

"""Problem Statement:"""
# Implement compress() and decompress() functions
# for a basic string compression scheme.
# In particular, we would like to compress strings
# with long runs of the same character, for example "aaabbbbbbccddddaa" into "a3b6c2d4a2".

def main():
    inputs = input()
    c = compress(inputs)
    decompress(c)

def compress(input):
    result = ""
    last_char = input[0]
    i = 0
    count = 1
    while i < len(input) - 2:
        if (input[i+1]) == last_char:
            count += 1
        else:
            result += last_char
            if count != 1:
                result += str(count)
            count = 1
            last_char = input[i+1]
        i += 1
    if input[i] == input[i+1]:
        count += 1
        result += last_char + str(count)
    else:
        result += last_char + input[i+1]
    return result

def decompress(inputs):
    result = ""
    i = 0
    while i < len(inputs) - 1:
        last_char = inputs[i]
        digits = ""
        if inputs[i+1].isnumeric():
            digits += inputs[i + 1]
            i += 1
            while i < len(inputs) - 1 and inputs[i + 1].isnumeric():
                digits += inputs[i + 1]
                i += 1
            result += last_char * int(digits)
        else:
            last_char = inputs[i+1]
            i += 1
    if inputs[len(inputs) - 1].isnumeric():
        pass
    else:
        result += inputs[len(inputs) - 1]
    return result


if __name__ == "__main__":
    main()
