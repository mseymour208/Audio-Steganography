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
i = len(secret)
#print(secret)

# I want to encode both channels so I can maximize capacity
# I want to iterate first through each sample, then through to both channels
# Creating a 1D view of data
# Extracting the first i elements
# Applying (sample & ~1) to clear LSB of first i elements
# .wav file is stereo, so two channels (N, 2)
# Flattening so I can iterate linearlly
# I clear each LSB and embed data, then overwrite the memory at flatView[idx]
flatView = data.ravel()
for idx in range(i):
    embedded = (flatView[idx] & ~1) | int(secret[idx])
    flatView[idx] = embedded

sio.wavfile.write('encodedFile.wav', rate, data)