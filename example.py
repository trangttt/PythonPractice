import re
import string
import sys 

swedish_consonants = ''.join(set(string.lowercase) - set('aeiouy'))

def encode_rovarspraket(msg):
    encode_consonant = lambda c: c.group(0) + 'o' + c.group(0).lower()
    return re.sub(r'(?i)[' + swedish_consonants + r']', encode_consonant, msg)

def decode_rovarspraket(msg):
    decode_consonant = lambda c: c.group(1)
    return re.sub(r'(?i)([' + swedish_consonants + r'])o\1', decode_consonant, msg)


if __name__ == "__main__" :
	print encode_rovarspraket(sys.argv[1])
