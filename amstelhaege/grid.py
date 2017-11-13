import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.ticker as plticker

eengezinswoning = [
    (0.856, 0.),   # left, bottom
    (0.856, 8.),  # left, top
    (8.856, 8.), # right, top
    (8.856, 0.),  # right, bottom
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

fig,ax=plt.subplots()

# Fixed spacing
plt.axis('scaled')

# Spacing between each line
intervals = 10

loc = plticker.MultipleLocator(base=intervals)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)

patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)

ax.grid(which='major', axis='both', linestyle='-')

# ax.grid(color='gray', linestyle='dashed')
ax.set_xlim(0, 160)
ax.set_ylim(0, 180)
plt.show()
