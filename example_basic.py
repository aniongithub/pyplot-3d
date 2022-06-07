from src.pyplot3d.basic import Cube
from src.pyplot3d.utils import ypr_to_R
import matplotlib.pyplot as plt

import numpy as np

# Initiate the plot
plt.style.use('seaborn')

fig = plt.figure()
ax = fig.gca(projection='3d')

# s1 = Sphere(ax, 1)
# s1.draw()

# R = ypr_to_R([0, 0, np.pi/2.0])
# p1 = Plane(ax, 3, 2, 'r', [0, 0, 1], R)
# p1.draw()

c1 = Cube(ax, [3, 4, 5])
# c1.draw_at([1,0,0], ypr_to_R([0,0,0]))
c1.draw_at([0,0,0], ypr_to_R([np.pi/4,0,0]))

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

plt.savefig("media/example_basic.png")