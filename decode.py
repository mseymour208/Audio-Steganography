import numpy as np
import scipy.io as sio

# Read in encoded wav
rate, encodedData = sio.wavfile.read('encodedFile.wav')
buffer = ""
header = 0

# Iterate data -> channel -> sample
i = 0
for channel in encodedData:
    # We've reached the end of the header
    if (i == 31):
        # Find length of encoded data & clear out buffer
        header = int(buffer, 2)
        buffer = ""
        i = 0

    # We've reached the end of encoded data
    if (i == (header - 1)):
        break

    for sample in channel:
        # Extract LSB
        LSB = (sample & 1)
        buffer += str(LSB)

print(buffer)

# iterate till i = 31, appending bits to buffer
# Convert buffer to int to get header
# Clear buffer
# Read number of bits in header
# Till i = header - 1