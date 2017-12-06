from random import randint

coords = [(25, 40), (102, 88), (14, 36)]

x = randint(0, 180)
y = randint(0, 160)

trigger = 0

for i in coords:
    xMIN = i[0]
    xMAX = i[0] + 8

    yMIN = i[1]
    yMAX = i[1] + bType.length

    if (xMIN <= x <= xMAX):
        trigger += 1
    if (yMIN <= y <= yMAX):
        trigger += 1

    if trigger == 2:
        x = randint(0, 180)
        y = randint(0, 160)
        print("changing chords")

print(x, y)
