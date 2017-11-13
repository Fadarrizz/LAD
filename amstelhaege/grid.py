import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

eengezinswoning = [
    (0., 0.),   # left, bottom
    (0., 8.),  # left, top
    (8., 8.), # right, top
    (8., 0.),  # right, bottom
    (0., 0.),   # ignored
]

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

path = Path(eengezinswoning, codes)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(0, 160)
ax.set_ylim(0, 180)
plt.show()
