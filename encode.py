import numpy as np
import scipy.io as sio
import customtkinter as ctk

# Reading in .wav file
rate, data = sio.wavfile.read('test.wav')

# Reading secret message from file
fileName = input("Name of txt file: ") + '.txt'
with open(fileName, 'r', encoding='utf-8') as file:
    msg = file.read()

# Converting the message string into a stream of bits
msgBytes = msg.encode('utf-8')
msgBits = ''.join(format(b, '08b') for b in msgBytes)

# Adding a 32 bit header to the secret data to denote message size in bits
# So the decoder knows when to stop reading from encoded file
header = np.binary_repr(len(msgBytes) * 8, width=32)
secret = header + msgBits
i = len(secret)

# Create a 1D view of data to iterate linearlly
flatView = data.ravel()
for idx in range(i):
    # Embedding one bit at a time
    # First clearing the LSB, then inserting our secret bit
    embedded = (flatView[idx] & ~np.int16(1)) | int(secret[idx])
    flatView[idx] = np.int16(embedded)

sio.wavfile.write('encodedFile.wav', rate, data)