import numpy as np

filename = "1.df"

data = np.fromfile(filename, dtype=np.float32)
data_shape = 32*32*32
len(data) - 32768
a = data[:6]
output = data[6:]
a.tofile("2.bin")
c = np.fromfile("2.bin",dtype=np.uint64)
print(c)
print(output.shape)