test = [0, 1, 2, 3, 4, 5]

trigger = True

while trigger:
    trigger = False

    for i in range(len(test)):
        print(i)
        if i == 4:
            print("break")
            i = 6
            trigger = True
            break

print("out of while")
