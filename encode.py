import numpy as np
import scipy.io as sio

# Reading in .wav file & secret message
rate, data = sio.wavfile.read('test.wav')
msg = input("Message to encode: ")

# Converting the message string into a stream of bits
msgBits = ''.join(format(ord(char), '08b') for char in msg)

# Adding a 32 bit header to the secret data to denote message size in bits
# So the decoder knows when to stop reading from encoded file
header = np.binary_repr(len(msg) * 8, width=32)
secret = header + msgBits
#print(secret)

# .wav file is stereo, so two channels
# I want to encode both channels so I can maximize capacity
# I want to iterate first through each sample, then through to both channels

i = 0
# Per channel, I want to perform these bitwise operations
for channel in data:
    # If we have reached the end of our message
    if i == (len(msg) * 8) - 1:
        break

    for sample in channel:
        # (sample & ~1) - Clears LSB of sample
        # (sample & ~1) | secret bit - Populates LSB with our data
        (sample & ~1) | secret[i]
    i += 1