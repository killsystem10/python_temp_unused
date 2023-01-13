import time

preh=0
nexh=0
battery=0
usebattery=0
savebattery=0
temp=0
high=[]

temp=int(input())
high=input().split()
high=list(map(int,high))
high.append(0)

for i in range(len(high)):
    preh=high[i]
    nexh=high[i+1]
    print(preh)
    print(nexh)
    if nexh==0:
        break
    else:
        if preh<nexh:
            temp=nexh-preh
            usebattery=usebattery+2*temp
            print(usebattery)
            print()
            time.sleep(1)
        elif preh>nexh:
            temp=preh-nexh
            temp=temp//2
            savebattery=savebattery+temp
            print(savebattery)
            print()
            time.sleep(1)

resultbattery=usebattery-savebattery
print()
print(resultbattery)