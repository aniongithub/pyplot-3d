from src.pyplot3d.camera import Camera
from src.pyplot3d.utils import ypr_to_R

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.gca(projection='3d')

camera = Camera(ax)
camera.draw_at([1, 1, 3], ypr_to_R([0, np.pi/4, 0]))

plt.savefig("media/example_camera.png")