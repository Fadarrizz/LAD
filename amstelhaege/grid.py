import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as plticker

fig, ax = plt.subplots()
house = {'house' : patches.Rectangle((20,20), 8, 8)}
for i in house:
    ax.add_artist(house[i])
    rx, ry = house[i].get_xy()
    cx = rx + house[i].get_width()/2.0
    cy = ry + house[i].get_height()/2.0
    house[i].set_color('green')

bungalow = {'bungalow' : patches.Rectangle((120, 120), 10, 7.5)}
for i in bungalow:
    ax.add_artist(bungalow[i])
    rx, ry = bungalow[i].get_xy()
    cx = rx + bungalow[i].get_width()/2.0
    cy = ry + bungalow[i].get_height()/2.0
    bungalow[i].set_color('purple')

maison = {'maison' : patches.Rectangle((80, 80), 11, 10.5)}
for i in maison:
    ax.add_artist(maison[i])
    rx, ry = maison[i].get_xy()
    cx = rx + maison[i].get_width()/2.0
    cy = ry + maison[i].get_height()/2.0
    maison[i].set_color('red')

plt.axis('scaled')

# Dashed grid lines
ax.grid(which='major', axis='both', linestyle='-')

# Spacing between each line
intervals = 10
loc = plticker.MultipleLocator(base=intervals)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)

ax.set_xlim(0, 180)
ax.set_ylim(0, 160)
plt.show()
