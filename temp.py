preh=0
nexh=0
battery=0
usebattery=0
savebattery=0
high=[10,6,10,6,8,15,10,13,12,20,0]








for i in range(11):
    preh=high[i]
    nexh=high[i+1]
    if nexh==0:
        break
    else:
        if preh<nexh:
            temp=nexh-preh
            usebattery=usebattery+2*temp
        elif preh>nexh:
            temp=preh-nexh
            temp=temp//2
            savebattery=savebattery+temp

resultbattery=usebattery-savebattery
print(resultbattery)