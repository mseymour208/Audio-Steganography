import numpy as np
import scipy.io as sio

# Read in encoded wav
rate, encodedData = sio.wavfile.read('encodedFile.wav')
buffer = ""
header = 0

# Iterate linearlly through encoded data
flatView = encodedData.ravel()
# Extract the 32 bit header
for idx in range(32):
    bit = (flatView[idx] & np.int16(1))
    buffer += bit
header = int(buffer, 2)
buffer = ""

# Start where header ended
for idx in range(32, header+1):
    # Extract each embedded bit
    bit = (flatView[idx] & np.int16(1))
    buffer += bit

print(buffer)

# iterate till i = 31, appending bits to buffer
# Convert buffer to int to get header
# Clear buffer
# Read number of bits in header
# Till i = header - 1