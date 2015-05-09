import ctypes




testLib = ctypes.cdll.LoadLibrary("test.dylib")

print testLib.get_random(3,5)



testLib.randomize()

print testLib.get_random(5,8)