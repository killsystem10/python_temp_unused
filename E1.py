preh = 0
nexh = 0
usebattery = 0
savebattery = 0
temp = 0

score = int(input())
high = input().split()
high = list(map(int, high))
high.append(-1)

for i in range(score):
    preh = high[i]
    nexh = high[i + 1]
    if nexh == -1:
        break
    else:
        if preh < nexh:
            temp = nexh - preh
            usebattery = usebattery + 2 * temp
        elif preh > nexh:
            temp = preh - nexh
            temp = temp // 2
            savebattery = savebattery + temp

resultbattery = usebattery - savebattery
print(resultbattery)
