import numpy as np

def loadDFandDFS(filename):
    data = np.fromfile(filename, dtype=np.float32)
    header = data[:6]
    header = header.tobytes()
    header = np.frombuffer(header, dtype=np.uint64)
    tmp_data = data[6:]
    return tmp_data.reshape(header)