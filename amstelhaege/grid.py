import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.ticker as plticker
from Classes import Building, House, Bungalow, Maison


house1 = House(100, 20, 8, 8, 4, 4)
x = house1.x
y = house1.y
a = house1.a
b = house1.b

pos = [
    ((x-a), (y-b)), # left, bottom
    ((x-a), (y+b)), # left, top
    ((x+a), (y+b)), # right, top
    ((x+a), (y-b)), # right, bottom
    (0., 0,)        # CLOSEPOLY
]

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

path = Path(pos, codes)

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
ax.set_xlim(0, 180)
ax.set_ylim(0, 160)
plt.show()
