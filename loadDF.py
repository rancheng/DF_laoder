import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm

filename = "1.df"

data = np.fromfile(filename, dtype=np.float32)
data_shape = 32 * 32 * 32
len(data) - 32768
a = data[:6]
output = data[6:]
a.tofile("2.bin")
c = np.fromfile("2.bin", dtype=np.uint64)
print(c)
print(output.shape)

sdf_filename = "1.sdf"
sdf_data = np.fromfile(sdf_filename, dtype=np.float32)
sdf_header = sdf_data[:6]
sdf_header = sdf_header.tobytes()
sdf_header = np.frombuffer(sdf_header, dtype=np.uint64)
tmp_sdf_data = sdf_data[6:]
tmp_sdf_data = tmp_sdf_data.reshape(sdf_header)

plot_sdf_data = np.isfinite(tmp_sdf_data)
color = tmp_sdf_data[np.isfinite(tmp_sdf_data)]

plot_sdf_data_inf = ~np.isfinite(tmp_sdf_data)
color_inf = tmp_sdf_data[~np.isfinite(tmp_sdf_data)]
norm = mpl.colors.Normalize(vmin=min(color), vmax=max(color))
cmap = cm.hot
m = cm.ScalarMappable(norm=norm, cmap=cmap)
plot_sdf_data = plot_sdf_data * 1
z, x, y = plot_sdf_data.nonzero()
z_inf, x_inf, y_inf = plot_sdf_data_inf.nonzero()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib as matplotlib


def color_map_color(value, cmap_name='jet', vmin=0, vmax=1):
    # norm = plt.Normalize(vmin, vmax)
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    cmap = cm.get_cmap(cmap_name)  # PiYG
    rgb = cmap(norm(abs(value)))[:3]  # will return rgba, we take only first 3 so we get rgb
    color = matplotlib.colors.rgb2hex(rgb)
    return color


fig = plt.figure("sdf data")
ax = fig.add_subplot(111, projection='3d')
color_list = []
for i in range(len(x)):
    color_list.append(m.to_rgba(color[i]))
ax.scatter(x, y, -z, zdir='z', c=color_list, s=0.6)

fig2 = plt.figure("inf part")
# color_list_inf = []
# for i in range(len(x)):
#     color_list_inf.append(m.to_rgba(color_inf[i]))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.scatter(x_inf, y_inf, -z_inf, zdir='z', c=cm.jet(color_inf), s=0.6)
plt.show()
