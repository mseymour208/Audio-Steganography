import numpy as np
import scipy.io as sio

# Reading in .wav file & secret message
testFile = sio.wavefile.read('test.wav')
secret = input("Message to encode: ")
print(secret)
