import numpy as np
import scipy.io as sio

# Reading in .wav file & secret message
testFile = sio.wavfile.read('test.wav')
msg = input("Message to encode: ")

# Converting the message string into a stream of bits
msgBits = ''.join(format(ord(char), '08b') for char in msg)

# Adding a 32 bit header to the secret data to denote message size in bits
# So the decoder knows when to stop reading from encoded file
header = np.binary_repr(len(msg) * 8, width=32)
secret = header + msgBits
print(secret)

