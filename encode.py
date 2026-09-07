import numpy as np
import scipy.io as sio

# Reading in .wav file & secret message
testFile = sio.wavfile.read('test.wav')
secret = input("Message to encode: ")
