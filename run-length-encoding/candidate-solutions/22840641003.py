#!/usr/bin/env python3

"""Problem Statement:"""
# Implement compress() and decompress() functions
# for a basic string compression scheme.
# In particular, we would like to compress strings
# with long runs of the same character, for example "aaabbbbbbcc" into "a3b6c2".

def main():
    inputs = input()
    return decompress(compress(inputs))

def compress(s):
    keep = {}
    keep = { 0: { 'letter': '', 'reps': 0}}
    index = 0
    result = ''
    
    for letter in s:
        if letter == keep[index]['letter']:
            keep[index]['reps'] +=1
                 
        else:
            index += 1
            keep[index] = { 'letter': letter, 'reps': 1}
    
    for index in range(1,len(keep)):
        result += keep[index]['letter']
        result += str(keep[index]['reps'])
        
    return(result)

def decompress(s):
    keep = { 0: { 'letter': '', 'reps': 0}}
    result = ''
    index = 0
           
    for i in s:
        if i.isalpha():
            index += 1
            keep[index] = { 'letter': i, 'reps': ''}
        else:
            keep[index]['reps'] += i
            
    for index in range(1,len(keep)):
        result += keep[index]['letter']*int(keep[index]['reps'])
        
    return(result)

if __name__ == "__main__":
    result = main()
    print(result)
