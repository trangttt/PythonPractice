
###########################################
##Using GENERATOR to save memory
###########################################
import logging

logging.basicConfig(level=logging.DEBUG)

def LCG(log_mod, a, c, seed ):
    logger = logging.getLogger(__name__)
    prev = seed
    mask = 2**log_mod - 1
    while True:
        prev = mask & (a * prev + c)
        for i in range(log_mod>>3):
            logger.debug('LCG {:3d}'.format((prev >> i*8) & 0xFF))
            yield (prev >> i*8) & 0xFF


def encode_bytes(bs, key):
    logger = logging.getLogger(__name__)
    logger.debug(bs)
    otp = LCG(32, 1664525, 1013904223, key)
    for b in bs:
        yield b ^ next(otp)

def encode(mes, key):
    return bytes(encode_bytes(mes.encode(), key))

def decode(ciph, key):
    return bytes(encode_bytes(ciph, key)).decode()

msg = "Attack at dawn"
key = 31337

#print(encode(msg,key))
print(decode(encode(msg, key), key))


############################################
##LESSONS LEARNED
##Convert string to bytes. number string.encode()
##

##########################################
#NAIVE
# key = 31337
# msg = "Attack at dawn"
#
# m = 2**31
# a = 65539
# c = 0
#
# def gen_random_number(len, key):
#     ret = []
#     x = key
#     for i in range(len):
#         ret.append((a*x+c)%m)
#     return ret
#
# def encrypt(mes, key):
#     n = len(mes)
#     otp = gen_random_number(n, key)
#     return " ".join([ str(ord(c) ^ otp[i]) for i, c in enumerate(mes)])
#
# def decrypt(ciph, key):
#     n = len(ciph.split())
#     otp = gen_random_number(n, key)
#     return "".join([ chr(int(c) ^ otp[i]) for i,c in enumerate(ciph.split())])
#
# cipher = encrypt(msg, key)
# print(cipher)
# print(decrypt(cipher, key))
